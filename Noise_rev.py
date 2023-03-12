import matplotlib.pyplot as plt
import numpy as np
from math import pi
import sounddevice as sd
import scipy.fftpack as sf
import scipy.signal as sig

plt.close('all')

#generating a signal
Fs = 200
t = 4
n = np.arange(0, t, 1/Fs)
f = 10
x = np.sin(2*pi*f*n)
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(n,x);plt.title('Sinusoidal Signal')
plt.xlabel('Time(s)');plt.ylabel('Amplitude')

#generate a noise
y = np.random.normal(0,1.5, np.size(x)) #additive white gaussian noise
x = x + y #noisy signal;

plt.subplot(3,1,2)
plt.plot(n,x);plt.title('Noisy Sinusoidal Wave')
plt.xlabel('Time(s)');plt.ylabel('Amplitude')


#take spectral analysis i.e suppose denies the signal
x_f = abs(sf.fft(x)) #FFT
l = np.size(x) #size
fr = (Fs/2)*np.linspace(0,1,4) #frequency axis,as FFT is double-sided but we've to take as single sided that's why frequency dovoded by 2
xl_m = (2/1)*abs(x_f[0:np.size(fr)]) #magnitude

plt.subplot(3,1,3)
plt.plot(fr,20*np.log10(xl_m));plt.title('Spectrum of noisy signal')
plt.xlabel('Frequency(Hz)');plt.ylabel('Magnitude')
plt.tight_layout()

#create a BPF

o = 5
fc = np.array([8,12]) #cutoff frequency
wc = 2*fc/Fs #into normal form
[b,a] = sig.butter(o, wc, btype = 'bandpass') #design a filter

#filter response
[w,h] = sig.freqz(b,a,worN= 1024)
w = Fs*w/(2*pi) #convert into hartz

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(w, 10*np.log10(h))
plt.title('Filter Frequency response')
plt.xlabel('Time(s)');plt.ylabel('Amplitude')


#filter signal

x_filt = sig.lfilter(b,a,x)
plt.subplot(2,1,2)
plt.plot(n,x_filt)
plt.title('Filtered signal')
plt.xlabel('Time(s)');plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()