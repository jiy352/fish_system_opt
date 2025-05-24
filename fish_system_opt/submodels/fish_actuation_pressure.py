import csdl
import numpy as np

class EelAmplitudeModel(csdl.Model):
    def initialize(self):
        # self.parameters.declare('num_eval', default=1)   # number of evaluation points
        self.parameters.declare('num_time_steps')          # Number of time samples
        self.parameters.declare('a_0', default=None)       # constant term
        self.parameters.declare('a_1', default=None)       # linear term

    def define(self):
        # num_eval = self.parameters['num_eval']
        num_time_steps = self.parameters['num_time_steps']
        a_0 = self.parameters['a_0']
        a_1 = self.parameters['a_1']
        
        # Inputs
        frequency = self.declare_variable('frequency')  # in Hz
        time_vector = self.declare_variable('time_vector', shape=(num_time_steps,)) 
        

        # Expand inputs
        f_expand = csdl.expand(frequency, shape=(num_time_steps, ))
        


        # 10 psi linear regression model: Amplitude = 27.903 - 6.430 * F

        # Outputs
        # amplitude = 27.903 - 6.430 * frequency
        amplitude = a_0 + a_1 * frequency
        amplitude_expand = csdl.expand(amplitude, shape=(num_time_steps,))/180*np.pi # convert to rad


        # Angle profile: theta(t) = A cos(2π f t)
        angle_profile = amplitude_expand * csdl.cos(2 * np.pi * f_expand * time_vector)

        # Time derivative: theta_dot(t) = -2π f A sin(2π f t)
        theta_dot = -2 * np.pi * f_expand * amplitude_expand * csdl.sin(2 * np.pi * f_expand * time_vector)

        # register outputs
        self.register_output('angle_profile', angle_profile)
        self.register_output('theta_dot', theta_dot)
        self.register_output('amplitude_deg', amplitude)
if __name__ == '__main__':
    import numpy as np
    import python_csdl_backend
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    # Constants
    num_time_steps = 500
    frequency_val = 1.0  # Hz

    # Time vector (0 to 1 second)
    time_vals = np.linspace(0, 1, num_time_steps)

    # Create model
    model = csdl.Model()
    model.add(
        EelAmplitudeModel(
            num_time_steps=num_time_steps,
            a_0=27.903,
            a_1=-6.430
        ),
        name='amplitude_model'
    )

    # Inputs
    model.create_input('frequency', val=frequency_val)
    model.create_input('time_vector', val=time_vals)

    # Run simulation
    sim = python_csdl_backend.Simulator(model)
    sim.run()

    # Extract outputs
    angle_profile = sim['angle_profile']
    theta_dot = sim['theta_dot']
    amplitude = sim['amplitude_deg']

    sim.check_partials(compact_print=True)

    # Plotting
    fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axs[0].plot(time_vals, angle_profile, label=f'θ(t), f = {frequency_val} Hz')
    axs[0].set_ylabel('Angle (deg)')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(time_vals, theta_dot, label='θ̇(t)', color='orange')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('θ̇ (deg/s)')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()
