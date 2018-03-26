for count in range(1010101010, 1389026623):
	a = count ** 2
	b = str(a)
	if count % 1000 == 0:
		print b
	if b[0] == '1':
		if b[2] == '2':
			if b[4] == '3':
				if b[6] == '4':
					if b[8] == '5':
						if b[10] == '6':
							if b[12] == '7':
								if b[14] == '8':
									if b[16] == '9':
										if b[18] == '0':
											print b
											break

