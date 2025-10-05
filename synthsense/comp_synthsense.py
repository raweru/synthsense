__all__ = ["synthsense"]

import logging
import dataclasses

from reinvent_plugins.normalize import normalize_smiles
from reinvent_plugins.components.synthsense.parameters import Parameters, split_params

from reinvent_plugins.components.synthsense.runner import run_aizynth

from ..add_tag import add_tag
from ..component_results import ComponentResults

logger = logging.getLogger("reinvent")


@add_tag("__component")
class synthsense:
    def __init__(self, params: Parameters):
        self.no_cache = True  # Skip scoring cache.
        self.params = params
        self.smiles_type = "rdkit_smiles"  # For the normalizer.
        logger.info("Initializing synthsense")
            
        self.params_run, self.endpoints = split_params(params)
        self.steps = 0
        self.number_of_endpoints = len(self.endpoints)

        logger.info(f"synthsense params: {params}, run params: {self.params_run}")

    @normalize_smiles
    def __call__(self, smilies: list[str]) -> ComponentResults:
        """Returns AiZynth score.

        This function assumes it will start one synthsense run,
        but we can extract multiple endpoints from one and the same run.
        """

        self.steps += 1
        out = run_aizynth(smilies, self.params_run, self.steps)

        # Here we can iterate over endpoints.
        # Component results are returned as a list of numpy arrays.
        # Each numpy array should be the size of `smilies`,
        # i.e. it should contain all scores for one endpoint.
        # Multiple endpoints go into the list as separate numpy arrays.
        all_scores = []
        for endpoint in self.endpoints:
            scores = endpoint.get_scores(smilies, out)
            all_scores.append(scores)

        return ComponentResults(
            scores=all_scores,
        )
