# Find spaceship on map that start in left bottom corner
astromap = '....\n..X.\n....'  # example astromap
print(astromap)


def find_spaceship(astromap):
    astromap = astromap.split('\n')
    astromap.reverse()
    for line in astromap:
        if 'X' in line:
            return [line.index('X'), astromap.index(line)]
    else:
        return "Spaceship lost forever."

# Test
print(find_spaceship(astromap))
