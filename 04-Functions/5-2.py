import converters

def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n/2.54

def ft_and_in_to_cm(ft, inch):
    return (ft * 12 + inch) * 2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')

print(f'2m = {m_to_cm(2)}cm')
print(f'532cm = {cm_to_m(532)}m')
print(f'100cm = {cm_to_in(100)}in') 
print(f'6ft 7in = {ft_and_in_to_cm(6, 7)}cm')