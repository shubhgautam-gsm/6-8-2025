def FarToCel(far):
    cel = (far - 32) * 5.0 / 9.0
    return cel

def CelToFar(cel):
    far = cel * 9.0 / 5.0 + 32
    return far