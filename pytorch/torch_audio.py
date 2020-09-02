import torch
import torchaudio

torchaudio.set_audio_backend('soundfile')

waveform, sample_rate = torchaudio.load('.wav')
torchaudio.save('_save.wav', waveform, sample_rate)