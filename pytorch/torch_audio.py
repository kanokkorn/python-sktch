import torch
import torchaudio
import matplotlib.pyplot as plt

torchaudio.set_audio_backend('soundfile')
waveform, sample_rate = torchaudio.load('data/Clover.flac')
print(f'Shape of waveform: {waveform.size()}')
print(f'Sample rate of waveform: {sample_rate}')

plt.figure()
plt.plot(waveform.t().numpy())
plt.show()