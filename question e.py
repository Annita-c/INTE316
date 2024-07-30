import numpy as np
import matplotlib.pyplot as plt

def compute_fft(signal, sample_rate):
    """
    Compute the Fast Fourier Transform of a signal.
    
    Parameters:
    signal (np.array): The input signal in the time domain.
    sample_rate (float): The sampling rate of the signal.
    
    Returns:
    freqs (np.array): Frequencies corresponding to the FFT values.
    fft_values (np.array): FFT values.
    """
    # Number of sample points
    n = len(signal)
    
    # Compute the FFT
    fft_values = np.fft.fft(signal)
    
    # Compute the corresponding frequencies
    freqs = np.fft.fftfreq(n, 1/sample_rate)
    
    # Only keep the positive frequencies and their corresponding FFT values
    pos_freqs = freqs[:n//2]
    pos_fft_values = np.abs(fft_values[:n//2]) * (2/n)  # Normalization
    
    return pos_freqs, pos_fft_values

def main():
    # Parameters
    f1 = 50  # Frequency of the first sine wave (Hz)
    f2 = 120  # Frequency of the second sine wave (Hz)
    sample_rate = 1000  # Sampling rate (Hz)
    duration = 1  # Duration of the signal (seconds)
    
    # Generate the time vector
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Generate the signal
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    # Compute the FFT
    freqs, fft_values = compute_fft(signal, sample_rate)
    
    # Plot the time-domain signal
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title("Time-Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Plot the frequency-domain signal
    plt.subplot(2, 1, 2)
    plt.stem(freqs, fft_values)
    plt.title("Frequency-Domain Signal (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    
    # Show the plots
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()

