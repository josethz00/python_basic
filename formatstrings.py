first_name = "José Thomaz"
last_name = "Antunes Soares"

output = "Hello, " + first_name+""+last_name
output2 = "Hello, {} {}".format(first_name, last_name)
output3 = "Hello, {0} {1}".format(first_name, last_name) #index parameter
output_short = f"Hello, {first_name} {last_name}"

print(output)
print(output2)
print(output3)
print(output_short)
