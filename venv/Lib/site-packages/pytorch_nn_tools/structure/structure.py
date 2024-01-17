from typing import List

import torch
from dataclasses import dataclass
from torch import nn


class NameGetter:
    def __init__(self, unnamed_template='unnamed_{count}_{type_name}'):
        self.count = 0
        try:
            unnamed_template.format(count=self.count, type_name="dummy2")
        except KeyError as e:
            raise ValueError("Invalid template '{}'. There is an issue with key: {}".format(unnamed_template, e))
        self.unnamed_template = unnamed_template

    def __call__(self, module):
        try:
            name = module.name
        except AttributeError:
            name = self.unnamed_template.format(count=self.count, type_name=type(module).__name__)
            self.count += 1
        return name


@dataclass
class LayerSize:
    name: str
    module: nn.Module
    size: torch.Size


def get_output_sizes(model, x) -> List[LayerSize]:
    sizes = []
    hooks = []
    get_name = NameGetter()

    def hook(module, input, output):
        name = get_name(module)
        sizes.append(LayerSize(name, module, output.size()))

    def register_hook(module):
        hooks.append(module.register_forward_hook(hook))

    # register hook
    model.apply(register_hook)

    # make a forward pass to trigger the hooks
    with torch.no_grad():
        model(x)

    # remove these hooks
    for h in hooks:
        h.remove()

    return sizes
