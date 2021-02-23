from env_config import  RUN_PARAMS
import os

def test_run():
    n = str(100)
    compute_qf = 'yes'

    params = {**RUN_PARAMS}

    if n is not None:
        params['GITCOIN_TIMESTEPS'] = n

    if compute_qf is not None:
        params['GITCOIN_COMPUTE_QF'] = compute_qf

    for (key, value) in params.items():
        os.environ[key] = value

    print("Preparing simulation")
    from model.run import run

    print("Run simuation")
    result = run()

