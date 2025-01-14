from . import extension  # noqa: F401
from torchaudio._internal import module_utils as _mod_utils  # noqa: F401
from torchaudio import (
    compliance,
    datasets,
    functional,
    models,
    kaldi_io,
    utils,
    sox_effects,
    transforms,
)

from torchaudio.backend import (
    list_audio_backends,
    get_audio_backend,
    set_audio_backend,
)

try:
    from .version import __version__, git_version  # noqa: F401
except ImportError:
    pass

__all__ = [
    'compliance',
    'datasets',
    'functional',
    'models',
    'kaldi_io',
    'utils',
    'sox_effects',
    'transforms',
    'list_audio_backends',
    'get_audio_backend',
    'set_audio_backend',
]
