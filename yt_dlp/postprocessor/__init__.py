# flake8: noqa: F401

from .common import PostProcessor
from .embedthumbnail import EmbedThumbnailPP
from .exec import ExecAfterDownloadPP, ExecPP
from .ffmpeg import (
    FFmpegConcatPP,
    FFmpegCopyStreamPP,
    FFmpegEmbedSubtitlePP,
    FFmpegExtractAudioPP,
    FFmpegFixupDuplicateMoovPP,
    FFmpegFixupDurationPP,
    FFmpegFixupM3u8PP,
    FFmpegFixupM4aPP,
    FFmpegFixupStretchedPP,
    FFmpegFixupTimestampPP,
    FFmpegMergerPP,
    FFmpegMetadataPP,
    FFmpegPostProcessor,
    FFmpegSplitChaptersPP,
    FFmpegSubtitlesConvertorPP,
    FFmpegThumbnailsConvertorPP,
    FFmpegVideoConvertorPP,
    FFmpegVideoRemuxerPP,
)
from .metadataparser import (
    MetadataFromFieldPP,
    MetadataFromTitlePP,
    MetadataParserPP,
)
from .modify_chapters import ModifyChaptersPP
from .movefilesafterdownload import MoveFilesAfterDownloadPP
from .sponskrub import SponSkrubPP
from .sponsorblock import SponsorBlockPP
from .xattrpp import XAttrMetadataPP
from ..plugins import load_plugins

_PLUGIN_CLASSES = load_plugins('postprocessor', 'PP')


def get_postprocessor(key):
    # TODO this is really hard to find, because I can't jump around using the class
    #  definition in IDEs, leaving me puzzled over how a specific post processor
    #  class ends up doing anything at all.
    return globals()[key + 'PP']


globals().update(_PLUGIN_CLASSES)
__all__ = [name for name in globals() if name.endswith('PP')]
__all__.extend(('PostProcessor', 'FFmpegPostProcessor'))
