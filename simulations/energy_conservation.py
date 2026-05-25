def test_energy_conservation():
    heat_in = 1000
    electrical = 300
    waste = 700

    assert abs(heat_in - (electrical + waste)) < 1e-6