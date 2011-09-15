import constants
from . import register_message_class
from . import Message
from . import UnsignedInt
from . import UnsignedIntMask
from . import Timestamp
from . import Bitfield
from . import CompletionCode
from . import Conditional
from . import RemainingBytes
from . import VariableByteArray
from pyipmi.utils import ByteBuffer
from pyipmi.errors import DecodingError, EncodingError

@register_message_class
class GetFruInventoryAreaInfoReq(Message):
    __cmdid__ = constants.CMDID_GET_FRU_INVENTORY_AREA_INFO
    __netfn__ = constants.NETFN_STORAGE
    __default_lun__ = 0
    __fields__ = (
        UnsignedInt('fru_id', 1, 0),
    )


@register_message_class
class GetFruInventoryAreaInfoRsp(Message):
    __cmdid__ = constants.CMDID_GET_FRU_INVENTORY_AREA_INFO
    __netfn__ = constants.NETFN_STORAGE | 1
    __default_lun__ = 0
    __fields__ = (
        CompletionCode(),
        UnsignedInt('area_size', 2),
        Bitfield('area_info', 1,
            Bitfield.Bit('access', 1),
            Bitfield.ReservedBit(7,0)
        ),
    )


@register_message_class
class ReadFruDataReq(Message):
    __cmdid__ = constants.CMDID_READ_FRU_DATA
    __netfn__ = constants.NETFN_STORAGE
    __default_lun__ = 0
    __fields__ = (
            UnsignedInt('fru_id', 1),
            UnsignedInt('offset', 2),
            UnsignedInt('count', 1),
    )


@register_message_class
class ReadFruDataRsp(Message):
    __cmdid__ = constants.CMDID_READ_FRU_DATA
    __netfn__ = constants.NETFN_STORAGE | 1
    __default_lun__ = 0

    def _length_count(obj):
        return obj.count

    __fields__ = (
            CompletionCode(),
            UnsignedInt('count', 1),
            VariableByteArray('data', _length_count),
    )


@register_message_class
class WriteFruDataReq(Message):
    __cmdid__ = constants.CMDID_WRITE_FRU_DATA
    __netfn__ = constants.NETFN_STORAGE
    __default_lun__ = 0

    __fields__ = (
        UnsignedInt('fru_id', 1),
        UnsignedInt('offset', 2),
        RemainingBytes('data'),
    )


@register_message_class
class WriteFruDataRsp(Message):
    __cmdid__ = constants.CMDID_WRITE_FRU_DATA
    __netfn__ = constants.NETFN_STORAGE | 1
    __default_lun__ = 0
    __fields__ = (
        CompletionCode(),
        UnsignedInt('count_written', 1)
    )
