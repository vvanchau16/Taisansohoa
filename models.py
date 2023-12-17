from pydantic import BaseModel
from typing import Optional

class QUYEN(BaseModel):
    MAQ: Optional[str] = None
    TenQ: str

class User(BaseModel):
    username: str
    password: str

class NCC(BaseModel):
    MANCC: Optional[str] = None  # Optional during creation
    TenNCC: str
    SDT: str
    EMAIL: str
    MST: str
    DC: str

class NV(BaseModel):
    MANV: Optional[str] = None
    TenNV: str
    SDT: str
    EMAIL: str
    DC: str
    STKNH: str
    MK: str

class PB(BaseModel):
    MAPB: Optional[str] = None
    TenPB: str

class KH(BaseModel):
    MAKH: Optional[str] = None  # Optional during creation
    TenKH: str
    SDT: str
    EMAIL: str
    MST: str
    DC: str

class TL(BaseModel):
    MATL: Optional[str] = None
    TenTL: str
    NgayTaiLen: str
    TepDinhKem: str

class HD(BaseModel):
    MAHD:Optional[str] = None
    TenHD: str
    NgayTao: str
    NgayTaiLen: str
    TepDinhKem: str

class TSCD(BaseModel):
    MATSCD: Optional[str]= None
    TenTSCD: str
    TT: str
    GiaTri: int
    THSD: int
    NgayMua: str
    KhauHao: int

class CCDC(BaseModel):
    MACCDC: Optional[str] = None
    TenCCDC: str
    TT: str
    GiaTri: int
class SP(BaseModel):
    MASP:Optional[str] = None
    TenSP: str
    DVT: str
    DG: int

class NVL(BaseModel):
    MANVL:Optional[str] = None
    TenNVL: str
    DVT: str
    DG: int

class DH(BaseModel):
    MADH:Optional[str]=  None
    NgayTao: str
    TongTien: int

class CTDH(BaseModel):
    MACTDH:Optional[str]=  None
    SL: int

class BB(BaseModel):
    MABB:Optional[str]=  None
    TenBB: str
    NgayViet: str
    NhaBao: str
    LinkBB: str

class VBPQ(BaseModel):
    MAVBPQ:Optional[str]=  None
    TenVBPQ: str
    NgayBH: str