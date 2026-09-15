from ../env/builder.py import make_builder
import numpy as np
from tampanda.symbolic.domains.blocks.blocks_domain import BlocksDomain

def collect_data(n=5):

    obj_list = []
    for i in range(n):
        builder = make_builder()

        # sampling
        rng = np.random.default_rng(seed)
        x = rng.uniform(0.30, 0.65)
        y = rng.uniform(-0.20, 0.20)
        pose = [x, y, 0.27]

        # 1,2: default block with size 4, and 6. 3-6: blocks from ycb for extended advanced test.
        """
        Name ID weights dims(mm)
        cube: 40
        block: 60
        gelatin: 9 Gelatin Box 97g 28 x 85 x 73
        pudding: 8 Pudding Box 187g 35 x 110 x 89
        wood: 36 Wood Block 729g 85 x 85 x 200
        bricks: 60 Foam Brick 28g 50 x 75 x 50
        69 Colored Wood Blocks 10.8g 26
        """
        idx = np.random.choice(np.arange(6), p=[0.4, 0.4, 0.05, 0.05, 0.08, 0.02]) # 0.28, 0.28, 0.15, 0.15, 0.02, 0.10, 0.02
        if idx == 0:
            builder.add_object("cube", pos=pose, name="block_a")
        elif idx == 1:
            builder.add_object("block", pos=pose, name="block_a")
        elif idx == 2:
            builder.add_object("pudding_box", pos=pose, name="block_a")
        elif idx == 3:
            builder.add_object("gelatin_box", pos=pose, name="block_a")
        elif idx == 4:
            builder.add_object("brick", pos=pose, name="block_a")
        elif idx == 5:
            builder.add_object("wood_block", pos=pose, name="block_a")

        # set block position within work space
        env = builder.build_env(rate=200.0)
        domain  = BlocksDomain(env.model, table_geom_name="table_surface")
        BOUNDS  = domain.get_working_bounds()        
        BLOCK_HALF = env.get_object_half_size("block_a")
        env.set_object_pose("block_a", np.array([x, y, BOUNDS["table_height"] + BLOCK_HALF[2] + 0.003]))
        env.reset_velocities(); env.forward(); env.rest(0.4)

        # obtain candidate data
        grasp_planner = GraspPlanner(table_z=0.00)
        pos  = env.get_object_position("block_a")
        half = env.get_object_half_size("block_a")
        quat = env.get_object_orientation("block_a")
        candidates = grasp_planner.generate_candidates(pos, half, quat)

        obj_list.append([pos, half, quat, candidates])

        print(f"working area x ∈ [{BOUNDS['min_x']:.2f},{BOUNDS['max_x']:.2f}], "
        f"y ∈ [{BOUNDS['min_y']:.2f},{BOUNDS['max_y']:.2f}], table_z={BOUNDS['table_height']:.3f}")

        show_views(env)
    return obj_list

if __name__ == "__main__":
    print(collect_data())
