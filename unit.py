import ants, importlib
importlib.reload(ants)
hive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
colony = ants.AntColony(None, hive, ants.ant_types(),
        ants.dry_layout, dimensions)
# Testing if queen will not crash with no one to buff
queen = ants.QueenAnt()
colony.places['tunnel_0_2'].add_insect(queen)
queen.action(colony)
# Attack a bee
bee = ants.Bee(3)
colony.places['tunnel_0_4'].add_insect(bee)
queen.action(colony)
bee.armor # Queen should still hit the bee
