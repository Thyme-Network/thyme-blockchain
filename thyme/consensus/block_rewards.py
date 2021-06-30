from thyme.util.ints import uint32, uint64

# 1 Thyme coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_thyme = 1000000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365
_halflife = 3
_coins_per_block = 5

def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 21:
        return uint64(int((7 / 8) * 2100000 * _mojo_per_thyme))
    elif height % 21000000 == 0:
        return uint64(int((7 / 8) * 210000 * _mojo_per_thyme))
    elif height % 2100000 == 0:
        return uint64(int((7 / 8) * 21000 * _mojo_per_thyme))
    elif height % 210000 == 0:
        return uint64(int((7 / 8) * 210 * _mojo_per_thyme))
    elif height % 21000 == 0:
        return uint64(int((7 / 8) * 21 * _mojo_per_thyme))
    else:
        return uint64(int((7 / 8) * 0.5 ** (height / (_halflife * _blocks_per_year)) * _coins_per_block * _mojo_per_thyme))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 21:
        return uint64(int((1 / 8) * 2100000 * _mojo_per_thyme))
    elif height % 21000000 == 0:
        return uint64(int((1 / 8) * 210000 * _mojo_per_thyme))
    elif height % 2100000 == 0:
        return uint64(int((1 / 8) * 21000 * _mojo_per_thyme))
    elif height % 210000 == 0:
        return uint64(int((1 / 8) * 210 * _mojo_per_thyme))
    elif height % 21000 == 0:
        return uint64(int((7 / 8) * 21 * _mojo_per_thyme))
    else:
        return uint64(int((1 / 8) * 0.5 ** (height / (_halflife * _blocks_per_year)) * _coins_per_block * _mojo_per_thyme))
