import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack
import ghostipy as gpy

class dsp():
    def __init__(self) -> None:
        pass
    
    def FFT(self, t, x):
        X = fftpack.fft(x)
        f = fftpack.fftfreq(t.size, t[1]-t[0])
        f = np.abs(f)
        return f, X
    
    def PSD(self, x, fs=1.0):
        f, Pxx = signal.welch(x, fs=fs, nperseg=x.length,
                                 noverlap=0,
                                 nfft=x.length,
                                 detrend='linear',
                                 scaling='density',
                                 axis=-1,
                                 window='hamming',
                                 return_onesided=True)

        return f, 20*np.log10(Pxx/np.max(Pxx))
    
    def Spect(x, fs):
        f, t, Sxx = signal.spectrogram(x,fs=fs,nperseg=1024,
                                         noverlap=0,
                                         nfft=1024,
                                         detrend='linear',
                                         scaling='density',
                                         axis=-1,window='hamming',
                                         return_onesided=True)
        return f, t, 20*np.log10(Sxx/np.max(Sxx))

    def WSST(self, x, fs=1.0):
        coefs, _, f, t, *_ = gpy.wsst(x, fs=fs, 
                                           freq_limits=[0, fs/2],
                                           boundary='zeros',
                                           window='hamming', 
                                           voices_per_octave=16,
                                           method='full')
        return 20*np.log10(coefs/np.max(coefs)), f, t
        
    def plot_time(self, t, x):
        plt.figure()
        plt.plot(t, x)
        plt.show()
        return
        
    def plot_frequency(self, f, X):
        plt.figure()
        plt.plot(f, X)
        plt.show()
        return
    
    def plot_timefreq(self, f, t, Sxx):
        plt.figure()
        plt.pcolormesh(t, f, Sxx)
        plt.show()
        return
    