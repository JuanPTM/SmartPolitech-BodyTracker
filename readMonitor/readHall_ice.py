# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.3
#
# <auto-generated>
#
# Generated from file `readHall.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module readHallComp
_M_readHallComp = Ice.openModule('readHallComp')
__name__ = 'readHallComp'

if 'Pos' not in _M_readHallComp.__dict__:
    _M_readHallComp.Pos = Ice.createTempClass()
    class Pos(object):
        def __init__(self, x=0.0, y=0.0, z=0.0):
            self.x = x
            self.y = y
            self.z = z

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_readHallComp.Pos):
                return NotImplemented
            else:
                if self.x != other.x:
                    return False
                if self.y != other.y:
                    return False
                if self.z != other.z:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_readHallComp._t_Pos)

        __repr__ = __str__

    _M_readHallComp._t_Pos = IcePy.defineStruct('::readHallComp::Pos', Pos, (), (
        ('x', (), IcePy._t_float),
        ('y', (), IcePy._t_float),
        ('z', (), IcePy._t_float)
    ))

    _M_readHallComp.Pos = Pos
    del Pos

if 'PersonInfo' not in _M_readHallComp.__dict__:
    _M_readHallComp.PersonInfo = Ice.createTempClass()
    class PersonInfo(object):
        def __init__(self, pos=Ice._struct_marker, id=0):
            if pos is Ice._struct_marker:
                self.pos = _M_readHallComp.Pos()
            else:
                self.pos = pos
            self.id = id

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_readHallComp.PersonInfo):
                return NotImplemented
            else:
                if self.pos != other.pos:
                    return False
                if self.id != other.id:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_readHallComp._t_PersonInfo)

        __repr__ = __str__

    _M_readHallComp._t_PersonInfo = IcePy.defineStruct('::readHallComp::PersonInfo', PersonInfo, (), (
        ('pos', (), _M_readHallComp._t_Pos),
        ('id', (), IcePy._t_int)
    ))

    _M_readHallComp.PersonInfo = PersonInfo
    del PersonInfo

if '_t_People' not in _M_readHallComp.__dict__:
    _M_readHallComp._t_People = IcePy.defineSequence('::readHallComp::People', (), _M_readHallComp._t_PersonInfo)

if 'hallPersons' not in _M_readHallComp.__dict__:
    _M_readHallComp.hallPersons = Ice.createTempClass()
    class hallPersons(object):
        def __init__(self, data=None):
            self.data = data

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_readHallComp.hallPersons):
                return NotImplemented
            else:
                if self.data != other.data:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_readHallComp._t_hallPersons)

        __repr__ = __str__

    _M_readHallComp._t_hallPersons = IcePy.defineStruct('::readHallComp::hallPersons', hallPersons, (), (('data', (), _M_readHallComp._t_People),))

    _M_readHallComp.hallPersons = hallPersons
    del hallPersons

if 'readHall' not in _M_readHallComp.__dict__:
    _M_readHallComp.readHall = Ice.createTempClass()
    class readHall(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_readHallComp.readHall:
                raise RuntimeError('readHallComp.readHall is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::readHallComp::readHall')

        def ice_id(self, current=None):
            return '::readHallComp::readHall'

        def ice_staticId():
            return '::readHallComp::readHall'
        ice_staticId = staticmethod(ice_staticId)

        def getHall(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_readHallComp._t_readHall)

        __repr__ = __str__

    _M_readHallComp.readHallPrx = Ice.createTempClass()
    class readHallPrx(Ice.ObjectPrx):

        def getHall(self, _ctx=None):
            return _M_readHallComp.readHall._op_getHall.invoke(self, ((), _ctx))

        def begin_getHall(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_readHallComp.readHall._op_getHall.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getHall(self, _r):
            return _M_readHallComp.readHall._op_getHall.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_readHallComp.readHallPrx.ice_checkedCast(proxy, '::readHallComp::readHall', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_readHallComp.readHallPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::readHallComp::readHall'
        ice_staticId = staticmethod(ice_staticId)

    _M_readHallComp._t_readHallPrx = IcePy.defineProxy('::readHallComp::readHall', readHallPrx)

    _M_readHallComp._t_readHall = IcePy.defineClass('::readHallComp::readHall', readHall, -1, (), True, False, None, (), ())
    readHall._ice_type = _M_readHallComp._t_readHall

    readHall._op_getHall = IcePy.Operation('getHall', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_readHallComp._t_hallPersons, False, 0), ())

    _M_readHallComp.readHall = readHall
    del readHall

    _M_readHallComp.readHallPrx = readHallPrx
    del readHallPrx

# End of module readHallComp
