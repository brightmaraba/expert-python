from sys import version_info
print(f'This is Python {version_info.major}.{version_info.minor}')

for x in range(10):
    print(f"10^{x} = {10**x:10d}")