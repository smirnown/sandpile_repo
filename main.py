from sandpile_driver import SandpileDriver

driver = SandpileDriver(
    size=5,
    max_grains_per_cell=3,
    iterations=5,
    source_coordinates_list=[(2, 2)]
    )
driver.execute_sandpile()