import noisereduce as nr
from pedalboard.io import AudioFile
from pedalboard import *



# Function to process audio


def process_audio(input_file):
    # Set sampling rate
    sr = 24000
    # Read audio file
    with AudioFile(input_file).resampled_to(sr) as f:
        audio = f.read(f.frames)

    # Reduce stationary noise
    reduced_noise = nr.reduce_noise(
        y=audio, sr=sr, stationary=True, prop_decrease=0.75)

    # Apply audio effects using pedalboard
    board = Pedalboard([
        NoiseGate(threshold_db=-30, ratio=1.5, release_ms=250),
        Compressor(threshold_db=-16, ratio=2.5),
        LowShelfFilter(cutoff_frequency_hz=400, gain_db=1, q=1),
        Gain(gain_db=1)
    ])

    processed_audio = board(reduced_noise, sr)

    return processed_audio, sr