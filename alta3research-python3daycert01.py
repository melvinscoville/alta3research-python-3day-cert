#!/usr/bin/env python3
"""alta3research-python3daycert01.py | Melvin Scoville | melvin.scoville@gmail.com
   Python script to generate OpenStack environment yaml output
   files using vm_list.csv input data."""

# standard library import
import csv

def main():
    """Function to generate yaml files"""
    # open our csv data (we want to loop across this)
    with open("vm_list.csv", "r") as csvfile:
        # counter to create unique file names
        i = 0
        # loop across our open file line by line
        for row in csv.reader(csvfile):
            i = i + 1 # increase i by 1 (to create unique admin.rc file names)
            filename = f"envFile{i}.yaml" # this f string says "fill in the value of i"
            
            # open a file via "with". This file will autoclose when the indentations stop
            with open(filename, "w") as yamlfile:
                # use the standard library print function to print our data
                # out to the open file open yamlfile (open in write mode)
                print(f"\nGenerating {filename} env yaml file.")
                print("parameter_defaults:", file=yamlfile)
                print("  # Environment variables for Heat template of Automation", file=yamlfile)
                print("\n  # VM related parameters", file=yamlfile)
                print("  name: " + row[0], file=yamlfile)
                print("  hostname: " + row[1], file=yamlfile)
                print("  flavor: " + row[2], file=yamlfile)
                print("  image_id: " + row[3], file=yamlfile)
                print("  server_group: " + row[4], file=yamlfile)
                print("  volume_id: " + row[5], file=yamlfile)
                print("\n  # Network Port", file=yamlfile)
                print("  private_port: " + row[6], file=yamlfile)
                print("\n  # Network interface", file=yamlfile)
                print("  private_ip: " + row[7], file=yamlfile)
                print("  private_netmask: " + row[8], file=yamlfile)
                print("  private_gateway: " + row[9], file=yamlfile)
                print(f"Completed {filename} env yaml file generation.")

if __name__ == "__main__":
    main()

# display this to the screen when all of the looping is over
print("\n### All env.yaml files created! ###\n")

# EOF