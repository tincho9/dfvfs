# -*- coding: utf-8 -*-
"""The BitLocker Drive Encryption (BDE) path specification implementation."""

from dfvfs.lib import definitions
from dfvfs.path import factory
from dfvfs.path import path_spec


class BdePathSpec(path_spec.PathSpec):
  """Class that implements the BDE path specification."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_BDE

  def __init__(self, parent=None, **kwargs):
    """Initializes the path specification object.

       Note that the BDE path specification must have a parent.

    Args:
      parent: optional parent path specification (instance of PathSpec).
              The default is None.

    Raises:
      ValueError: when parent is not set.
    """
    if not parent:
      raise ValueError(u'Missing parent value.')

    super(BdePathSpec, self).__init__(parent=parent, **kwargs)

  @property
  def comparable(self):
    """Comparable representation of the path specification."""
    return self._GetComparable()


# Register the path specification with the factory.
factory.Factory.RegisterPathSpec(BdePathSpec)