###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
a_side_string = input('Enter cube side a: ')
b_side_string = input('Enter cude side b:')
c_side_string = input('Enter. cube sode c:')
cuboid_side_a = int(a_side_string)
cuboid_side_b = int(b_side_string)
cuboid_side_c = int(c_side_string)
cuboid_volume =  cuboid_side_a * cuboid_side_b * cuboid_side_c
cuboid_surface_area = 2 * (cuboid_side_a * cuboid_side_b) + 2 * (cuboid_side_a * cuboid_side_c) + 2 * (cuboid_side_b * cuboid_side_c)
print(f'The volume of a cuboid with sides is {cuboid_volume}')
print(f'The surface of a cuboid with sides is {cuboid_surface_area}')