import csdl
import numpy as np

class EelAmplitudeModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_time_steps')
        self.parameters.declare('a_0', default=None)
        self.parameters.declare('a_1', default=None)
        self.parameters.declare('seg_names', default=None)  # list of segment names
        self.parameters.declare('phi', default=None)        # list of phase shifts (radians)

    def define(self):
        num_time_steps = self.parameters['num_time_steps']
        a_0 = self.parameters['a_0']
        a_1 = self.parameters['a_1']
        seg_names = self.parameters['seg_names']
        phi = self.parameters['phi']

        # Inputs
        frequency = self.declare_variable('frequency')  # in Hz
        time_vector = self.declare_variable('time_vector', shape=(num_time_steps,))

        # Amplitude (converted to radians)
        amplitude = (a_0 + a_1 * frequency) / 180 * np.pi
        amplitude_expand = csdl.expand(amplitude, shape=(num_time_steps,))
        f_expand = csdl.expand(frequency, shape=(num_time_steps,))

        # Loop through segments and assign phase
        for i, seg_name in enumerate(seg_names):
            if i<2:
                phase =  phi[i]  # accumulate phase shift
                angle = amplitude_expand * csdl.cos(2 * np.pi * f_expand * time_vector + phase)
                theta_dot = -2 * np.pi * f_expand * amplitude_expand * csdl.sin(2 * np.pi * f_expand * time_vector + phase)

                self.register_output(f'{seg_name}_theta', angle)
                self.register_output(f'{seg_name}_theta_dot', theta_dot)
            else:
                pass

        # Also output raw amplitude for reference
        self.register_output('amplitude_deg', amplitude * 180 / np.pi)


if __name__ == '__main__':
    import numpy as np
    import python_csdl_backend
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False

    # Setup
    num_time_steps = 70
    frequency_val = 1.0
    time_vals = np.linspace(0, 1, num_time_steps)

    # # Segment names and phase shifts (e.g., segment_0 leads by π/2)
    # seg_names = ['seg_0', 'seg_1', 'seg_2']
    # phi = [np.pi/2, np.pi/4, 0]  # seg_0 leads seg_1 by π/2, seg_1 leads seg_2 by π/4

    # Segment names and phase shifts (e.g., segment_0 leads by π/2)
    seg_names = ['seg_0', 'seg_1']
    phi = [np.pi/2, 0]  # seg_0 leads seg_1 by π/2, seg_1 leads seg_2 by π/4


    # Model
    model = csdl.Model()
    model.add(
        EelAmplitudeModel(
            num_time_steps=num_time_steps,
            a_0=27.903,
            a_1=-6.430,
            seg_names=seg_names,
            phi=phi
        ),
        name='amplitude_model'
    )

    model.create_input('frequency', val=frequency_val)
    model.create_input('time_vector', val=time_vals)

    sim = python_csdl_backend.Simulator(model)
    sim.run()

    # Plot results
    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    for seg in seg_names:
        axs[0].plot(time_vals, sim[f'{seg}_theta'], label=f'{seg}_theta')
        axs[1].plot(time_vals, sim[f'{seg}_theta_dot'], label=f'{seg}_theta_dot')

    axs[0].set_ylabel('Angle (rad)')
    axs[1].set_ylabel('Angular Velocity (rad/s)')
    axs[1].set_xlabel('Time (s)')
    axs[0].legend()
    axs[1].legend()
    axs[0].grid(True)
    axs[1].grid(True)
    plt.tight_layout()
    plt.show()
