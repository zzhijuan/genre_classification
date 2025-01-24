import pytest
import pandas as pd
import wandb


run = wandb.init(project="exercise_9", job_type="data_tests")


def pytest_addoption(parser):
    parser.addoption("--reference_artifact", action="store")
    parser.addoption("--sample_artifact", action="store")

    # COMPLETE HERE: add the option for ks_alpha
    parser.addoption("--ks_alpha", action="store")

@pytest.fixture(scope="session")
def data(request):

    reference_artifact = request.config.option.reference_artifact

    if reference_artifact is None:
        pytest.fail("--reference_artifact missing on command line")

    sample_artifact = request.config.option.sample_artifact

    if sample_artifact is None:
        pytest.fail("--sample_artifact missing on command line")

    local_path = run.use_artifact(reference_artifact).file()
    sample1 = pd.read_csv(local_path)

    local_path = run.use_artifact(sample_artifact).file()
    sample2 = pd.read_csv(local_path)

    return sample1, sample2


@pytest.fixture(scope='session')
def ks_alpha(request):

    # COMPLETE HERE: read the option ks_alpha from the command line,
    # and return it as a float
    ks_alpha_threshold = request.config.option.ks_alpha
    if ks_alpha is None:
        pytest.fail("--ks_threshold missing on command line")

    return float(ks_alpha_threshold)
    
