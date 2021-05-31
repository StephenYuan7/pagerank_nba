function NLQos()
{
	this.clientID = null;
	var m_videoTrackerMap = {};
	
	this.initialized = false;
	
	this.initialize = function(config)
	{
		if(!NLQosTracker.initialized)
		{
			NLQosTracker.initialized = true;
			var params = {appVersion:"v5",receiverURL: config.locQos,siteID:config.site,productID:"website"};
			if(config.appVersion!=null)
				params.appVersion = config.appVersion;
			if(config.appName!=null)
				params.productID = config.appName;
			if(config.uid!=null)
				params.userID = config.uid;
			if(config.userType!=null)
				params.userType = config.userType;
			if(config.tlid!=null)
				params.loginID = config.tlid;
			if(config.mvpduserid!=null)
				params.mvpdUserID = config.mvpduserid;
			if(config.xuID!=null)
				params.xuID = config.xuID;
			if(config.appType!=null)
				params.appType = config.appType;
			if(config.deviceType!=null)	
				params.deviceType = config.deviceType;
			if(config.qosInterval!= null)
				params.vHBInterval = config.qosInterval;
			if(config.networkType!=null)
				params.networkType = config.networkType;
			if(config.extClientID!=null)
				params.clientID = config.extClientID;
			if(config.freePreview!=null)
				params.freePreview = config.freePreview;
				
			window.nltrack.init(params);
			window.nltrack.callbackError = this.errorHandler;
			
			this.clientID = nltrack.getClientID();
		}
	};
	
	this.reInit = function(config)
	{
		var params = {};
		if(config.networkType != null)
			params.networkType = config.networkType;
		if(config.uid!=null)
			params.userID = config.uid;
		if(config.userType!=null)
			params.userType = config.userType;
		if(config.tlid!=null)
			params.loginID = config.tlid;
		if(config.mvpduserid!=null)
			params.mvpdUserID = config.mvpduserid;
		if(config.xuID!=null)
			params.xuID = config.xuID;
		if(config.appVersion!=null)
			params.appVersion = config.appVersion;
		if(config.custom!=null)
			params.custom = config.custom;
		if(config.extClientID!=null)
			params.clientID = config.extClientID;
		if(config.freePreview!=null)
			params.freePreview = config.freePreview;
		
		if(config.productID!=null)
			params.productID = config.productID;
		else
			params.productID = "Chromecast";
			
		window.nltrack.reInit(params);
	};

	this.reset = function(config)
	{
		this.initialized = false;
		this.deleteVideoTracker(config);
	}
	
	this.createVideoTracker = function(config)
	{
		var t = new NLQosVideoTracker(config);
		m_videoTrackerMap[config.playerId] = t;
		
		return t;
	};
	
	this.deleteVideoTracker = function(config)
	{
		if(m_videoTrackerMap[config.playerId] != null)
		{
			m_videoTrackerMap[config.playerId].destroy();
			m_videoTrackerMap[config.playerId] = null;
		}
	};
	
	this.getVideoTracker = function(playerId)
	{
		if(m_videoTrackerMap!=null)
		{
			var t = m_videoTrackerMap[playerId];
			if(t!=null)
				return t;
			else
				return null;
		}	
		else
			return null;
	};
	
	this.errorHandler = function(msg)
	{
		console.log("[Error]:",msg);
	};
	
	this.trackPage = function(pageName)
	{
		try 
		{
			if(nltrack)
				nltrack.onPageOpen({name:pageName});
		}
		catch(err){}	
	};
	
	this.trackLogin = function(id, type, tlid)
	{
		try 
		{
			if(nltrack)
			{
				var params = {userID:id};
				if(type!=null)
					params.userType = type;
				if(tlid!=null)
					params.loginID = tlid;
				
				nltrack.onLogin(params);
			}	
		}
		catch(err){}		
	};
	
	this.trackMVPDLogin = function(mvpdId, mvpdUserId, userType)
	{
		try 
		{
			if(nltrack)
			{
				var params = {userID:mvpdId, userType:userType?userType:'mvpdsubscriber'};
				if(mvpdUserId)
					params.mvpdUserID = mvpdId+':'+mvpdUserId;
				
				nltrack.onLogin(params);
			}	
		}
		catch(err){}		
	};
	
	this.trackLogout = function()
	{
		try 
		{
			if(nltrack)
				nltrack.onLogout();
		}	
		catch(err){}	
	};

	this.trackCustomAppEvent = function(eventName, info)
	{
		try 
		{
			if(nltrack)
			{
				if(eventName == "search")
				{
					if(info!=null && info.keyword!=null && info.keyword.length>0)
						nltrack.onSearch({keyword:info.keyword.toString()});
				}
			}
		}
		catch(err){}
	};
	
	this.trackRegistration = function(username)
	{
		try
		{
			if(nltrack && username && username.length>0)
				nltrack.onAccountCreation({registrationUsername:username});
		}
		catch(err){}
	};
	
	this.trackPurchaseSelection = function(info)
	{
		if(nltrack && info)
		{
			var order = {};
			order.sku = info.sku;
			order.name = info.skuName;
			order.currency = info.currency;
			order.price = parseFloat(info.price);
			order.ppv = info.ppv;
			
			try {
				nltrack.onPurchaseSelection(order);
			}
			catch(err){}	
		}
	};
	
	this.trackPurchaseBilling = function(info)
	{
		if(nltrack && info)
		{
			var order = {};
			order.sku = info.sku;
			order.name = info.skuName;
			order.currency = info.currency;
			order.price = parseFloat(info.price);
			order.ppv = info.ppv;
			
			try {
				nltrack.onPurchaseBilling(order);
			}
			catch(err){}	
		}
	};
	
	this.trackPurchaseConfirmation = function(info)
	{
		if(nltrack && info)
		{
			var order = {};
			order.sku = info.sku;
			order.name = info.skuName;
			order.currency = info.currency;
			order.orderTotal = parseFloat(info.orderTotal);
			order.orderID = info.orderid;
			order.ppv = info.ppv;
			
			try {
				if(info.isReg && info.username && info.username.length>0)
					nltrack.onAccountCreation({registrationUsername:info.username});
				nltrack.onPurchaseConfirmation(order);
			}
			catch(err){}	
		}
	};
	
	this.trackError = function(err)
	{
		if(nltrack && err)
		{
			var error = {};
			error.errorType = err.type;
			error.errorMsg = err.description;
			
			try {
				nltrack.onError(error);
			}
			catch(err){}	
		}
	};
	
	this.trackVideoClick = function(info)
	{
		if(nltrack && info)
		{
			var videoInfo = {};
			videoInfo.page    	  = info.page;
        	videoInfo.section 	  = info.section;
        	videoInfo.contentId   = info.id;
        	videoInfo.contentType = info.type;
        	videoInfo.recommendListId = info.recommendListId;
			
			try {
				nltrack.onVideoClick(videoInfo);
			}
			catch(err){}	
		}
	};
}

function NLQosVideoTracker(config)
{	
	var m_player = config.playerId;
	var m_videoTracker = null;
	var m_heartBeatMsg = null;
	var m_videoOpened = false;
	var m_cdnMap = null;
	
	var DATA_TYPE_AD = "ad";
	var DATA_TYPE_VIDEO = "video";
	
	var vs = {LIVE:1, DVR_LIVE:2, ARCHIVE:3};
	
	var params = {
		playerVersion:config.playerId,
		productID:config.playerId
	};
	if(config.playerName!=null)
		params.productID = config.playerName;
	if(config.deviceType !=null && config.deviceType == "Chromecast")
	{
		params.playerVersion = "Chromecast";
		delete params.productID;
	}
	
	m_videoTracker = nltrack.createVideoTracker(params);
		
	document.addEventListener('nlvideostart',nlTrackVideoStart);
	document.addEventListener('nlvideocomplete',nlTrackVideoEnd);
	document.addEventListener('nlvideopercent',nlTrackVideoPercent);
	document.addEventListener('nlvideoduration',nlTrackVideoDuration);
	document.addEventListener('nlvideostate',nlTrackVideoState);
	document.addEventListener('nlvideostatus',nlTrackVideoStatus);
	document.addEventListener('nlvideoerror',nlTrackVideoError);
	document.addEventListener('nlstreamrating',nlTrackVideoRating);
	document.addEventListener('nladstart',nlTrackAdStart);
	document.addEventListener('nladpause',nlTrackAdPause);
	document.addEventListener('nladresume',nlTrackAdResume);
	document.addEventListener('nladcomplete',nlTrackAdComplete);
	document.addEventListener('nlcustomevent',nlTrackCustomEvent);

	this.destroy = function()
	{
		document.removeEventListener('nlvideostart',nlTrackVideoStart);
		document.removeEventListener('nlvideocomplete',nlTrackVideoEnd);
		document.removeEventListener('nlvideopercent',nlTrackVideoPercent);
		document.removeEventListener('nlvideoduration',nlTrackVideoDuration);
		document.removeEventListener('nlvideostate',nlTrackVideoState);
		document.removeEventListener('nlvideostatus',nlTrackVideoStatus);
		document.removeEventListener('nlvideoerror',nlTrackVideoError);
		document.removeEventListener('nlstreamrating',nlTrackVideoRating);
		document.removeEventListener('nladstart',nlTrackAdStart);
		document.removeEventListener('nladpause',nlTrackAdPause);
		document.removeEventListener('nladresume',nlTrackAdResume);
		document.removeEventListener('nladcomplete',nlTrackAdComplete);
		document.removeEventListener('nlcustomevent',nlTrackCustomEvent);
	}
	
	this.updatePlayheadTime = function(time)
	{
		if(m_videoOpened)
		{
			var hb = getHeartBeatMsg();
			hb.currentPlayPosition = Math.round(time);
			try
			{
				if(hb!= null && m_videoTracker)
					m_videoTracker.onVideoStatusChange(getHeartBeatMsg());
			}
			catch(err){}
		}	
	}
	
	var m_contentStarted = false;
	function nlTrackVideoStart(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			m_heartBeatMsg = {};
			setHeartBeatMsg(DATA_TYPE_VIDEO, data);
			onVideoOpen();
		}	
	}
	
	function nlTrackVideoEnd(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
		    m_videoOpened = false;
			m_heartBeatMsg = null;
			m_contentStarted  = false;
			
			try
			{
				if(m_videoTracker)
					m_videoTracker.onVideoStop();
			}
			catch(err){}		
		}	
	}
	
	function nlTrackVideoPercent(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			var param = {percentage:data.value};
			try
			{			 
				if(m_videoTracker)
					m_videoTracker.onVideoMilestone(param);
			}
			catch(err){}
		}
	}
	
	function nlTrackVideoDuration(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			setHeartBeatMsg(DATA_TYPE_VIDEO, data);
			var hb = getHeartBeatMsg();
			try 
			{
				if(m_videoTracker && data.video.droppedFrameCount!=null)
				{
					if(hb.oldDropFrameCount != null)
					{
						if(data.video.droppedFrameCount > hb.oldDropFrameCount)
							hb.newDropFrameCount = data.video.droppedFrameCount - hb.oldDropFrameCount;
						else
							hb.newDropFrameCount = 0;
									
						hb.oldDropFrameCount = data.video.droppedFrameCount;
					}	
					else
					{
						hb.newDropFrameCount = data.video.droppedFrameCount;
						hb.oldDropFrameCount = data.video.droppedFrameCount;
					}
				}
				if(m_videoTracker && data.video.bufferTime!=null)
				{
					var currentBufferTime = parseInt(data.video.bufferTime*1000);
					if(hb.oldBufferTime != null)
					{
						if(currentBufferTime > hb.oldBufferTime)
							hb.bufferTime = currentBufferTime - hb.oldBufferTime;
						else
							hb.bufferTime = 0;
									
						hb.oldBufferTime = currentBufferTime;
					}	
					else
					{
						hb.bufferTime    = currentBufferTime;
						hb.oldBufferTime = currentBufferTime;
					}
				}
				if(m_videoTracker && data.video.bytesLoaded!=null && m_cdnMap!=null)
				{
					var trafficArray = [];
					for(var i=0;i<data.video.bytesLoaded.length;i++)
					{
						var trafficObj = {};
						var cdnName = data.video.bytesLoaded[i].cdnName;
						
						if(m_cdnMap[cdnName] == null)
						{
							m_cdnMap[cdnName] = {
								bytes:data.video.bytesLoaded[i].bytes
							};
							trafficObj.cdnName = cdnName.toString();
							trafficObj.bytes   = data.video.bytesLoaded[i].bytes
						}
						else
						{
							trafficObj.cdnName = cdnName.toString();
							var newBytes = data.video.bytesLoaded[i].bytes;
							var oldBytes = m_cdnMap[cdnName].bytes;
						
							if(newBytes > oldBytes)
								trafficObj.bytes = newBytes - oldBytes;
							else
								trafficObj.bytes = 0;
										
							m_cdnMap[cdnName].bytes = newBytes;
						}
						trafficArray.push(trafficObj);
					}
					hb.newTraffic = trafficArray;
				}
				m_videoTracker.onVideoStatusChange(hb);
				clearVideoStatusParams();
			}
			catch(err){}	
		}		
	}
	
	function nlTrackVideoState(event)
	{
		var data = nlGetMetadata(event);
		if(m_videoTracker && m_videoOpened && isValidInstance(data))
		{
			switch(data.value)
			{
				case "playing":
					if(!m_contentStarted)
					{
						m_contentStarted = true;
						try {
							var hb = getHeartBeatMsg();
							
							// To fix bitrate not being reported on first HB call
							nlTrackVideoStatus(event);
							
							m_videoTracker.onVideoStart(hb);
						}
						catch(err){}
					}
					else
					{	
						try {
							m_videoTracker.onVideoResume();
						}
						catch(err){}
					}
					break;
				case "paused":
					try {
						m_videoTracker.onVideoPause();
					}
					catch(err){}	
					break;
				case "disconnected":
					try {
						if(m_contentStarted)
							nlTrackVideoEnd(event);
					}
					catch(err){}	
					break;
			}
		}
	}
	
	function nlTrackVideoStatus(event)
	{
		var data = nlGetMetadata(event);
		if(m_heartBeatMsg && isValidInstance(data))
		{
			setHeartBeatMsg(DATA_TYPE_VIDEO, data);
			var hb = getHeartBeatMsg();
			
			switch(data.property)
			{
				case "windowMode":
					hb.windowMode = data.value;
					break;
					
				case "bitrate":
					var value = parseInt(data.value);
					if(!isNaN(value))
						hb.bitrate = value;
					break;
					
				case "bandwidth":
					hb.bandwidth = data.value;
					break;
					
				case "newDropFrameCount":
					var value = parseInt(data.value);
					if(!isNaN(value))
						hb.newDropFrameCount = value;
					break;
					
				case "bufferTime":
					var value = parseInt(data.value);
					if(!isNaN(value))
						hb.bufferTime = value;
					break;
			}
			
			try 
			{
				if(m_videoTracker)
				{
					m_videoTracker.onVideoStatusChange(hb);
					clearVideoStatusParams();
				}	
			}
			catch(err){}		
		}		
	}
	
	function nlTrackVideoError(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			m_heartBeatMsg = {};
			setHeartBeatMsg(DATA_TYPE_VIDEO, data);
			
			var error = {errorCode:data.value, errorMsg:data.message};

			if(data.errorURL!=null && data.errorURL.length>0)
				error.errorURL = data.errorURL;

			try
			{			 
				if(m_videoTracker)
				{
					onVideoOpen();
					m_videoTracker.onVideoError(error);
				}
			}
			catch(err){}	
		}	
	}

	function nlTrackVideoRating(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			try
			{
				if(m_videoTracker)
					m_videoTracker.onStreamRating({score:data.value});
			}
			catch(err){}
		}	
	}
	
	function nlTrackAdStart(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			m_heartBeatMsg = {};
			setHeartBeatMsg(DATA_TYPE_AD, data);
			
			try
			{
				if(m_videoTracker)
					m_videoTracker.onADStart(getHeartBeatMsg());
			}
			catch(err){}
		}	
	}
	
	function nlTrackAdComplete(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			setHeartBeatMsg(DATA_TYPE_AD, data);
			try 
			{
				if(m_videoTracker)
					m_videoTracker.onADStop(getHeartBeatMsg());
			}
			catch(err){}		
		}		
	}
	
	function nlTrackAdPause(event)
	{
		
	}

	function nlTrackAdResume(event)
	{
		
	}
	
	function nlTrackCustomEvent(event)
	{
		var data = nlGetMetadata(event);
		if(isValidInstance(data))
		{
			switch(data.event)
			{
				case "videochanged":
					nlTrackVideoEnd(event);
					break;
					
				case "midrollcomplete":
					setHeartBeatMsg(DATA_TYPE_VIDEO, data);
					break;
			}
		}
	}
	
	function clearVideoStatusParams()
	{
		var hb = getHeartBeatMsg();
		
		if(hb)
		{
			if(hb.bitrate != null)
				delete hb.bitrate;
				
			if(hb.bandwidth != null)
				delete hb.bandwidth;
				
			if(hb.newDropFrameCount != null)
				delete hb.newDropFrameCount;
				
			if(hb.bufferTime != null)
				delete hb.bufferTime;
				
			if(hb.newTraffic != null)
				delete hb.newTraffic;
		}	
	}
	
	function setHeartBeatMsg(type,data)
	{
		if(m_heartBeatMsg && data)
		{
			m_heartBeatMsg.id = parseInt(data.video.id);
			m_heartBeatMsg.type = data.video.type;
			if(data.video.extid != null)
				m_heartBeatMsg.extid = data.video.extid.toString();
			
			if(type == DATA_TYPE_AD)
			{
				m_heartBeatMsg.adType = data.ad.type;
				if(data.video.type == "game")
					m_heartBeatMsg.gt = data.video.game.gt;
					
				if(m_heartBeatMsg.windowMode==null)
					m_heartBeatMsg.windowMode = "normal";
			}
			else if(type == DATA_TYPE_VIDEO)
			{
				m_heartBeatMsg.cameraAngle = (data.video.cam)?data.video.cam:-1;	//m_heartBeatMsg.cam is deprecated
				m_heartBeatMsg.currentPlayPosition = Math.round(data.video.playheadTime);
				m_heartBeatMsg.streamURL = (data.video.publishPoint!=null)?data.video.publishPoint:"";
				m_heartBeatMsg.streamLength = data.video.duration;
				m_heartBeatMsg.streamDescription = data.video.name;
				
				if(data.video.startupTime!=null)
					m_heartBeatMsg.startupTime = data.video.startupTime;
				
				if(data.video.isAudio)
					m_heartBeatMsg.audio = true;
				
				if(data.video.type == "game")
				{	
					for(var prop in data.video.game)
						m_heartBeatMsg[prop] = data.video.game[prop];
				}
				
				m_heartBeatMsg.vs = vs.ARCHIVE;
				if(data.video.live)
				{
					m_heartBeatMsg.vs = vs.LIVE;
					if(data.video.dvr)
					{
						m_heartBeatMsg.vs = vs.DVR_LIVE;
						if(data.video.dvrSt!=null)
							m_heartBeatMsg.st = data.video.dvrSt;	
						if(data.video.dvrDur!=null)
							m_heartBeatMsg.dur = data.video.dvrDur;
					}
				}
				if(data.video.epgShowName!=null)
					m_heartBeatMsg.epgShowName = data.video.epgShowName;
					
				if(data.video.epgShowTime!=null)
					m_heartBeatMsg.epgShowTime = data.video.epgShowTime;
				
				m_heartBeatMsg.isAdaptive = (data.video.isAdaptive)?true:false;
				
				if(data.video.bitrate!=null)
					m_heartBeatMsg.bitrate = data.video.bitrate;
					
				if(data.video.bandwidth!=null)
					m_heartBeatMsg.bandwidth = data.video.bandwidth;
					
				if(data.video.bufferTime!=null)
					m_heartBeatMsg.bufferTime = data.video.bufferTime;
					
				if(m_heartBeatMsg.windowMode==null)
					m_heartBeatMsg.windowMode = "normal";

				if(data.video.contentCategory!=null)
					m_heartBeatMsg.contentCategory = data.video.contentCategory;

				if(data.video.autoplay!=null)	//number, 1 - Yes, 0 - No
					m_heartBeatMsg.autoplay = data.video.autoplay;
			}
		}
	}
	
	function getHeartBeatMsg()
	{
		return m_heartBeatMsg;
	}
	
	function onVideoOpen()
	{
		var hb = getHeartBeatMsg();
		if(hb && !m_videoOpened)
		{
			try 
			{
				m_videoTracker.onVideoOpen(hb);
				m_videoOpened = true;
				m_cdnMap = {};
			}
			catch(err){}	
		}	
	}
	
	function isValidInstance(data)
	{
		if(data)
			return data.htmlid == m_player;
		else
			return false;
	}
	
	function nlGetMetadata(event)
	{
		if(event!=null)
		{
			var data = event.detail.data;
			return data;
		}
		else
			return null;	
	}
}
var NLQosTracker = new NLQos();
if(window.NL && typeof NL.require != 'undefined')
	NL.define(NLQosTracker);
