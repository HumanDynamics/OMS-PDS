__author__ = 'jbt'
import pdb
import time
# motion data is included for localhost testing purposes, since the iOS simulator doesn't produce it.
#uniques = {
#    'motion': { 'attitude_pitch': 0.733424593851337,
#                'attitude_x': -0.2209912033994121,
#                'attitude_yaw': 0.08644265799832047,
#                'datetime': '2014-08-28 13:51',
#                'gravity_x': -0.1628383100032806,
#                'gravity_y': -0.6694176197052002,
#                'gravity_z': -0.7248197793960571,
#                'probe': 'motion',
#                'rotationRate_x': 0.02880095317959785,
#                'rotationRate_y': 0.5419228076934814,
#                'rotationRate_z': 0.01222392171621323,
#                'userAcceleration_x': 0.06832537800073624,
#                'userAcceleration_y': 0.06832537800073624,
#                'userAcceleration_z': 0.06832537800073624},
#}

def getfunfdata(data):

    devtype = data['probe']
    if devtype== 'deviceinfo':
        funfdata = deviceinfo(data)
        return funfdata
    #if devtype == 'motion':
    #    funfdata = motion(data)
    #    return
    if devtype == 'positioning':
        funfdata = positioning(data)
        return funfdata
    else:
        return {}


def deviceinfo(data):
    if data['brightness'] > 0:
        brightness = True
    else:
        brightness = False
    model = []
    model.append(data['device_model'])
    model.append(data['system_version'])
    model = ' '.join(model)

    try:
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S:%f'))) - time.timezone
    except Exception as e:
        pdb.set_trace()
        print "\n\n EXCEPT 1 STATEMENT ENTERED\n\n"
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M'))) - time.timezone
    except Exception as e:
        pdb.set_trace()
        print "\n\n EXCEPT 2 STATEMENT ENTERED\n\n"
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S'))) - time.timezone
    except:
        print "\n\n EXCEPT ELSE DEVICEINFO STATEMENT ENTERED\n\n"
        print "datetime could not be parsed"
        print data
        print data['datetime']

    ScreenProbe = {"edu.mit.media.funf.probe.builtin.ScreenProbe": {
    "_id": {
      "$oid": "540a1d3791cfc86cda607ef4"
    },
    "key": "edu.mit.media.funf.probe.builtin.ScreenProbe",
    "time": datetime,
    "value": {
      "screen_on": brightness,
      "timestamp": datetime
    }
    }
    }

    HardwareInfoProbe = {"edu.mit.media.funf.probe.builtin.HardwareInfoProbe": {
    "_id": {
      "$oid": "5407294791cfc81dda355f43"
    },
    "key": "edu.mit.media.funf.probe.builtin.HardwareInfoProbe",
    "time": datetime,
    "value": {
      "androidid": " ",
      "bluetoothmac": " ",
      "brand": " ",
      "deviceid": " ",
      "model": model,
      "timestamp": datetime,
      "wifimac": " "
    }
  }
  }

    dinfo = ScreenProbe.copy()
    dinfo.update(HardwareInfoProbe)

    return dinfo


def positioning(data):
    altitude = data['altitude']
    course = data['course']
    try:
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S:%f'))) - time.timezone
    except Exception as e:
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M'))) - time.timezone
    except Exception as e:
        datetime = int(time.mktime(time.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S'))) - time.timezone
    except:
        print "datetime could not be parsed"
        print data
        print data['datetime']

    horacc = data['horizontal_accuracy']
    lat = data['lat']
    lon = data['lon']

    SimpleLocation = {"edu.mit.media.funf.probe.builtin.SimpleLocationProbe": {
    "_id": {
      "$oid": "540a2b2491cfc86cda608135"
    },
    "key": "edu.mit.media.funf.probe.builtin.SimpleLocationProbe",
    "time": datetime,
    "value": {
      "maccuracy": horacc,
      "maltitude": altitude,
      "mbearing": course,
      "mdistance": 0,
      "melapsedrealtimenanos": {
        "$numberLong": " "
      },
      "mhasaccuracy": False,
      "mhasaltitude": False,
      "mhasbearing": False,
      "mhasspeed": False,
      "minitialbearing": 0,
      "misfrommockprovider": False,
      "mlat1": 0,
      "mlat2": 0,
      "mlatitude": lat,
      "mlon1": 0,
      "mlon2": 0,
      "mlongitude": lon,
      "mprovider": " ",
      "mresults": [
        0,
        0
      ],
      "mspeed": 0,
      "mtime": {
        "$numberLong": " "
      },
      "timestamp": datetime
    }
  }
    }
    print SimpleLocation
    return SimpleLocation


def insertblankdata():
    blanks = {
          "edu.mit.media.funf.probe.builtin.BluetoothProbe": {
    "_id": {
      "$oid": "5408e7d991cfc86cda603ad6"
    },
    "key": "edu.mit.media.funf.probe.builtin.BluetoothProbe",
    "time": 0.0,
    "value": {
      "android-bluetooth-device-extra-class": {
        "mclass": 0
      },
      "android-bluetooth-device-extra-device": {
        "maddress": " "
      },
      "android-bluetooth-device-extra-rssi": 0,
      "timestamp": 0.0
    }
  },
   "edu.mit.media.funf.probe.builtin.CallLogProbe": {
    "_id": {
      "$oid": " "
    },
    "key": "edu.mit.media.funf.probe.builtin.CallLogProbe",
    "time": 0.0,
    "value": {
      "_id": 1252,
      "date": {
        "$numberLong": ""
      },
      "duration": 0,
      "number": "",
      "numbertype": "",
      "timestamp": 0.0,
      "type": 0
    }
  },
    "edu.mit.media.funf.probe.builtin.RunningApplicationsProbe": {
    "_id": {
      "$oid": " "
    },
    "key": "edu.mit.media.funf.probe.builtin.RunningApplicationsProbe",
    "time": 0.0,
    "value": {
      "duration": 0.0,
      "taskinfo": {
        "baseintent": {
          "maction": " ",
          "mcategories": [
            " "
          ],
          "mcomponent": {
            "mclass": " ",
            "mpackage": " "
          },
          "mflags": 0
        },
        "id": 0,
        "persistentid": 0,
        "stackid": 0
      },
      "timestamp": 0.0
    }
  },
     "edu.mit.media.funf.probe.builtin.SmsProbe": {
    "_id": {
      "$oid": "5409040e91cfc86cda60413d"
    },
    "key": "edu.mit.media.funf.probe.builtin.SmsProbe",
    "time": 0.0,
    "value": {
      "address": " ",
      "body": " ",
      "date": {
        "$numberLong": " "
      },
      "locked": False,
      "person": " ",
      "protocol": 0,
      "read": False,
      "reply_path_present": False,
      "service_center": " ",
      "status": 0,
      "thread_id": 0,
      "timestamp": 0.0,
      "type": 0
    }
  },
  "edu.mit.media.funf.probe.builtin.WifiProbe": {
    "_id": {
      "$oid": "540a2b2491cfc86cda608133"
    },
    "key": "edu.mit.media.funf.probe.builtin.WifiProbe",
    "time": 0.0,
    "value": {
      "bssid": " ",
      "capabilities": " ",
      "distancecm": 0,
      "distancesdcm": 0,
      "frequency": 0,
      "level": 0,
      "ssid": " ",
      "timestamp": 0.0,
      "wifissid": {
        "octets": {
          "buf": [],
          "count": 0
        }
      }
    }
  }
}

    return blanks

