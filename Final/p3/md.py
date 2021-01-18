import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.constants as CONSTANTS
import math
import json
import os


class SingleAtomMD:
    def __init__(self, length, number, mu, mass, k, v_max, radii, T, h=10 ** -3, saving_period=10, name='MD'):
        self.length = length
        self.length_half = self.length / 2
        self.number = number
        self.mu = mu
        self.mass = mass
        self.k = k
        self.v_max = v_max
        self.radii = radii
        self.T = T
        self.h = h
        self.h_half = h / 2
        self.saving_period = saving_period
        self.name = name
        self.reduced_time = 0
        self._file_base_name = f'{self.name}_{self.length}_{self.number}_{v_max}_{self.h}_{radii}'

        self.positions = np.zeros((2, self.number))
        self._place_particles_regularly()
        self._periodic_boundaries()

        self.radii_sizes = np.zeros(self.number)
        self._assign_random_radii()

        self.velocities = np.zeros((2, self.number))
        self._assign_initial_velocities()
        self._center_of_mass_frame()

        self._positions_diff = np.zeros((2, self.number, self.number))
        self._update_positions_diff()

        self._adjacency_matrix = np.zeros((self.number, self.number))
        self._update_adjacency_matrix()

        self.accelerators = np.zeros((2, self.number))
        self._update_accelerators()

        self._reduced_temperature = None
        self._reduced_volume = None

        self._initialize_files()

    def _assign_random_radii(self):
        n = int(self.number / len(self.radii))
        self.radii_sizes = np.repeat(self.radii, n)
        np.random.shuffle(self.radii_sizes)

    def _initialize_files(self):
        file = open(f'{self._file_base_name}.info', 'w')
        info = {
            'length': self.length,
            'number': self.number,
            'mu': self.mu,
            'mass': self.mass,
            'k': self.k,
            'v_max': self.v_max,
            'radii': self.radii,
            'T': self.T,
            'h': self.h,
            'saving_period': self.saving_period,
            'data_size': np.dtype(float).itemsize,
            'trajectory': ['positions', 'velocities'],
            'data': ['temperature', 'mean_neighbors']
        }
        json.dump(info, file, indent=True)
        file.close()

        file = open(f'{self._file_base_name}.traj', 'wb')
        self._update_trajectory_file(file)
        file.close()

        file = open(f'{self._file_base_name}.data', 'wb')
        self._update_data_file(file)
        file.close()

    def _update_positions_diff(self):
        for axis in range(2):
            tiled_positions = np.tile(self.positions[axis], (self.number, 1))
            np.subtract(tiled_positions, np.transpose(tiled_positions), self._positions_diff[axis])

        far_positive_indexes = self._positions_diff > self.length_half
        self._positions_diff[far_positive_indexes] -= self.length
        far_negative_indexes = self._positions_diff < -self.length_half
        self._positions_diff[far_negative_indexes] += self.length

    def _update_positions_and_distances(self):
        self._periodic_boundaries()
        self._update_positions_diff()
        self._update_adjacency_matrix()

    def _periodic_boundaries(self):
        out_indexes = self.positions > self.length
        self.positions[out_indexes] -= self.length
        out_indexes = self.positions < 0
        self.positions[out_indexes] += self.length

    def _generate_noises(self):
        return np.random.normal(0, 1, (2, self.number)) * np.sqrt(2 * self.mu * self.T / self.h)

    def _update_accelerators(self):
        self.accelerators = -self.mu * self.velocities + self._generate_noises() - self.k * np.sum(self._adjacency_matrix * self._positions_diff, axis=1)

    def _update_adjacency_matrix(self):
        self._adjacency_matrix[:] = 0
        tiled_radii = np.tile(self.radii_sizes, (self.number, 1))
        total_radii = tiled_radii + np.transpose(tiled_radii)

        distances = np.sqrt(np.sum(np.square(self._positions_diff), axis=0))
        neighbors_indexes = distances < total_radii
        self._adjacency_matrix[neighbors_indexes] = 1
        np.fill_diagonal(self._adjacency_matrix, 0)

    @staticmethod
    def _write_list_in_file(file, list):
        file.write(list.tobytes())

    def _update_trajectory_file(self, file):
        for position in self.positions:
            self._write_list_in_file(file, position)
        for velocity in self.velocities:
            self._write_list_in_file(file, velocity)

    def _get_data_list(self):
        return np.array([
            self.get_reduced_temperature(),
            self.get_mean_neighbor(),
        ], dtype=float)

    def _update_data_file(self, file):
        self._write_list_in_file(file, self._get_data_list())

    def _time_step(self):
        print(f'\rTime: {self.reduced_time}', end='')
        accelerators_changes = self.accelerators * self.h_half
        self.positions += (self.velocities + accelerators_changes) * self.h
        self.velocities += accelerators_changes
        self._update_positions_and_distances()
        self._update_accelerators()
        self.velocities += self.accelerators * self.h_half
        self.reduced_time += 1

        self._reduced_temperature = None

    def render(self, reduced_time, flush_period=10000):
        trajectory_file = open(f'{self._file_base_name}.traj', 'ab')
        data_file = open(f'{self._file_base_name}.data', 'ab')
        flush_numbers = int(reduced_time / flush_period)
        extra_time = reduced_time % flush_period
        for flush_step in range(flush_numbers):
            for step in range(flush_period):
                self._time_step()
                if self.reduced_time % self.saving_period == 0:
                    self._update_trajectory_file(trajectory_file)
                    self._update_data_file(data_file)
            trajectory_file.flush()
            os.fsync(trajectory_file.fileno())
            data_file.flush()
            os.fsync(data_file.fileno())
        for step in range(extra_time):
            self._time_step()
            if self.reduced_time % self.saving_period == 0:
                self._update_trajectory_file(trajectory_file)
                self._update_data_file(data_file)

        print(end='\n')
        trajectory_file.close()
        data_file.close()

        return DataAnalysis(self._file_base_name)

    def _center_of_mass_frame(self):
        velocity_mean = np.mean(self.velocities, axis=1)
        for axis in range(2):
            self.velocities[axis] -= velocity_mean[axis]

    def _place_particles_regularly(self):
        self.positions = np.random.rand(2, self.number) * self.length

    def _assign_initial_velocities(self):
        max_amp = np.ones(self.number) * self.v_max
        for axis in range(2 - 1):
            random_thetas = np.random.rand(self.number) * (2 * np.pi)
            self.velocities[axis] = max_amp * np.cos(random_thetas)
            max_amp = max_amp * np.sin(random_thetas)
        self.velocities[-1] = max_amp

    def get_reduced_temperature(self):
        if self._reduced_temperature is None:
            self._reduced_temperature = np.sum(np.square(self.velocities)) / ((self.number - 1) * 2)

        return self._reduced_temperature

    def get_mean_neighbor(self):
        return np.mean(np.sum(self._adjacency_matrix, axis=1))


class DataAnalysis:
    def __init__(self, file_base_name):
        self.file_base_name = file_base_name
        info = self._process_info_file()
        self.length = info['length']
        self.number = info['number']
        self.mu = info['mu']
        self.mass = info['mass']
        self.k = info['k']
        self.v_max = info['v_max']
        self.radii = info['radii']
        self.T = info['T']
        self.h = info['h']
        self.saving_period = info['saving_period']
        self.data_size = info['data_size']
        self.trajectory_struct = info['trajectory']
        self.data_struct = info['data']
        self._pos_vel_size = 2 * self.number * self.data_size
        self._traj_batch_size = len(self.trajectory_struct) * self._pos_vel_size
        self._data_batch_size = len(self.data_struct) * self.data_size
        self.sample_numbers = int(os.stat(f'{self.file_base_name}.data').st_size / self._data_batch_size)

        self._reduced_temperature = None
        self._reduced_temperature_error = None
        self._mean_neighbor = None
        self._mean_neighbor_error = None
        self._equilibrium_index = self.sample_numbers / 2

    def _process_info_file(self):
        file = open(f'{self.file_base_name}.info', 'r')
        info = json.load(file)
        file.close()
        return info

    def auto_correlation(self, show=False):
        if show or self._relaxation_index is None:
            THERESHOLD = np.exp(-1)
            velocity_diff = self.trajectory_struct.index('velocities') * self._pos_vel_size
            temperature_diff = self.data_struct.index('temperature') * self.data_size
            trajectory_file = open(f'{self.file_base_name}.traj', 'rb')
            data_file = open(f'{self.file_base_name}.data', 'rb')

            steps = np.arange(0, int(self.sample_numbers / 5), dtype=int)
            C_v = np.zeros(len(steps))
            for step in steps:
                T_total = 0
                for sample in range(self.sample_numbers - step):
                    trajectory_file.seek(sample * self._traj_batch_size + velocity_diff)
                    data_file.seek(sample * self._data_batch_size + temperature_diff)
                    T_total += np.frombuffer(data_file.read(self.data_size))
                    velocities_1 = np.frombuffer(trajectory_file.read(self._pos_vel_size))
                    trajectory_file.seek((sample + step) * self._traj_batch_size + velocity_diff)
                    velocities_2 = np.frombuffer(trajectory_file.read(self._pos_vel_size))
                    C_v[step] += np.sum(velocities_1 * velocities_2)
                C_v[step] /= (T_total * 2 * (self.number - 1))
                if C_v[step] <= THERESHOLD and self._relaxation_index is None:
                    self._relaxation_index = step
                    if not show:
                        break

            if self._relaxation_index is None:
                self._relaxation_index = math.ceil(-steps[-1] / np.log(C_v[-1]))

            times = steps * (self.saving_period * self.h)

            if show:
                plt.plot(times, C_v)
                plt.xlabel(r'Time $(\times \tau)$')
                plt.ylabel(r'$C_v$')
                plt.savefig(f'{self.file_base_name}_c_v.jpg')
                plt.show()

            trajectory_file.close()
            data_file.close()

        return self._relaxation_index * self.saving_period * self.h

    def animate(self, interval=50):
        file = open(f'{self.file_base_name}.traj', 'rb')
        data = open(f'{self.file_base_name}.data', 'rb')
        positions_diff = self.trajectory_struct.index('positions') * self._pos_vel_size

        def update_frame(sample, frame, ax):
            file.seek(sample * self._traj_batch_size + positions_diff)
            positions = np.frombuffer(file.read(self._pos_vel_size))
            frame.set_data(positions[:self.number], positions[self.number:2 * self.number])
            # ax.set_title(r'Time $(\times \tau):$' + f'{round(sample * self.saving_period * self.h, 2)}')
            data.seek(sample * self._data_batch_size)
            ax.set_title(r'T :' + f'{round(np.frombuffer(data.read(self.data_size))[0], 2)} K')
            return frame,

        fig = plt.figure()
        ax = plt.gca()
        frame, = plt.plot([], [], linestyle='', marker='o')
        plt.xlim(0, self.length)
        plt.ylim(0, self.length)
        ani = animation.FuncAnimation(fig, update_frame, self.sample_numbers, fargs=(frame, ax), interval=interval,
                                      blit=True)
        ani.save(f'{self.file_base_name}.mp4')
        file.close()

    def _data_property_values(self, property_name):
        data = open(f'{self.file_base_name}.data', 'rb')
        property_diff = self.data_struct.index(property_name) * self.data_size
        values = np.zeros(self.sample_numbers)
        samples = range(self.sample_numbers)

        for sample in samples:
            data.seek(sample * self._data_batch_size + property_diff)
            values[sample] = np.frombuffer(data.read(self.data_size))

        data.close()

        return values

    def _calc_data_property_mean(self, property_name):
        values = self._data_property_values(property_name)
        valid_values = values[self._equilibrium_index:]
        mean_value = np.mean(valid_values)
        error = np.std(valid_values, ddof=1) / np.sqrt(len(values))
        return mean_value, error

    def get_reduced_temperature(self):
        if self._reduced_temperature is None:
            self._reduced_temperature, self._reduced_temperature_error = self._calc_data_property_mean('temperature')

        return np.array([self._reduced_temperature, self._reduced_temperature_error])

    def get_mean_neighbor(self):
        if self._mean_neighbor is None:
            self._mean_neighbor, self._mean_neighbor_error = self._calc_data_property_mean('mean_neighbors')

        return np.array([self._mean_neighbor, self._mean_neighbor_error])

    def get_reduced_temperature_values(self):
        return self._data_property_values('temperature')

    def get_mean_neighbor_values(self):
        return self._data_property_values('mean_neighbors')

    def plot_temperature(self):
        temperatures = self.get_reduced_temperature_values()
        times = np.arange(self.sample_numbers) * self.saving_period * self.h

        plt.plot(times, temperatures)
        plt.xlabel(r'Time $(\times \tau)$')
        plt.ylabel(r'T $(\times \epsilon / k_B)$')
        plt.savefig(f'{self.file_base_name}_temperatures.jpg')
        plt.show()

    def plot_mean_neighbors(self):
        mean_neighbors = self.get_mean_neighbor_values()
        times = np.arange(self.sample_numbers) * self.saving_period * self.h

        plt.plot(times, mean_neighbors)
        plt.xlabel(r'Time $(\times \tau)$')
        plt.ylabel(r'Mean Neighbors')
        plt.savefig(f'{self.file_base_name}_mean_neighbors.jpg')
        plt.show()
