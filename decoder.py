from numpy.fft import fft

decoded_frequencies = ''


def decode_fft(y_data, list_chars, fs=10000):
	global decoded_frequencies
	sample_length = len(y_data)

	T = 0.04
	N = int(fs * T)
	step = N

	start = 0
	end = N
	decoded_sting = ''
	for c in range(0, int(sample_length / step)):

		z = y_data[start:end]
		yf = fft(z)
		start += step
		end += step

		index = int(fs / step)
		freq = []
		for i in range(5, int(len(yf))):
			if int(abs(yf[i])) > 1:
				freq.append(i * index)

		low = freq[0]
		middle = freq[1]
		high = freq[2]

		# print("low {}, middle {}, high {}".format(low, middle, high))

		decoded_frequencies = decoded_frequencies + "low {}, middle {}, high {}".format(low, middle, high)
		# print("low {}, middle {}, high {}".format(low, middle, high))
		# print(decoded_frequencies)
		for i in range(0, len(list_chars)):
			if (list_chars[i]['low'] == low) & (list_chars[i]['middle'] == middle) & (
				 list_chars[i]['high'] == high):
				# print(list_chars[i]['char'])
				decoded_frequencies = decoded_frequencies + " => '{}'\n".format(list_chars[i]['char'])
				decoded_sting += list_chars[i]['char']


	return decoded_sting , decoded_frequencies


	