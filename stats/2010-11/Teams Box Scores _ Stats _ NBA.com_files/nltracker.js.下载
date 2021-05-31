function NLTracker()
{
	this.initialized = false;

	this.initialize = function(config)
	{
		this.config = config;

		if(window.NL && typeof window.NL.require != "undefined")
		{
			initializeLater(config);
		}
		else
		{
			nlLoadScript(config.locResource+"scripts/require.js");
			setTimeout(function(){initializeLater(config)},200);
		}
	};

	var requireLoaded = 0;
	function initializeLater(config)
	{
		if(!window.NL || typeof window.NL.require == "undefined")
		{
			if((requireLoaded++)<100)
				setTimeout(function(){initializeLater(config)},100);
			else
				setTimeout(function(){initializeLater(config)},5000);
		}
		else
		{
			NLTracker.initialized = true;
			NL.require.config({
				paths:
						{
							nlbase: config.locResource + "scripts",
							CMSDK : config.locResource + "scripts/CMSDK"
						},
				shim :
						{
							"nlbase/nlqos"     :{ deps : [ "nlbase/nltrack.min"] },
							"nlbase/comscore"  :{ deps : [ "nlbase/streamsense.min"] },
							"nlbase/nlcomscore2"  :{ deps : [ "nlbase/streamsense2.min"] },
							"nlbase/nlcomscore3"  :{ deps : [ "nlbase/comscorelib"] },
							"nlbase/nladobeheartbeat"  :{ deps : [ "nlbase/VideoHeartbeat.min"]},
							"nlbase/nlcatchmedia"  :{ deps : [ "CMSDK"] }
						}
			});

			NL.requirejs.onError = function (err)
			{
				console.log(err.requireType);
			};

			var hasGA = false;
			if(isFlash(config))
			{
				if(config.gaa!=null && (config.comscore!=null || config.externalTrackCallback!=null || config.nielsen!=null || config.heartbeat!=null||config.personalization!=null))
					hasGA = true;
			}
			else if(config.gaa!=null)
				hasGA = true;

			if(typeof NLGATracker != 'undefined')
			{
				NLGATracker.initialize(config);
				if(hasGA && config.playerId!=null)
					NLGATracker.createVideoTracker(config);
			}
			else if(config.gaa!=null)
			{
				NL.require(["nlbase/nlga"],function(ga){
					if(ga)
					{
						NLGATracker.initialize(config);
						if(config.playerId!=null && hasGA)
							NLGATracker.createVideoTracker(config);
					}
				});
			}

			if(config.locQos!=null && config.locQos.toString().length>0)
			{
				NL.require(["nlbase/nlqos", "nlbase/nltrack.min"],function(qos){
							if(qos)
							{
								NLQosTracker.initialize(config);
								if(!isFlash(config) && config.playerId!=null)
									NLQosTracker.createVideoTracker(config);

								// QoS client ID is required for CM to set the silentUserID
								nlInitializeCatchMediaTracker(config);
							}
						},
						function(error){
							// If QoS JS is not loaded
							nlInitializeCatchMediaTracker(config);
						});
			}
			else // If QoS is not a requirement
			{
				nlInitializeCatchMediaTracker(config);
			}
			if(config.comscore!=null)
			{
				if(!Array.isArray(config.comscore))
				{
					var comscorelib = ["nlbase/nlcomscore3"];
					NL.require(comscorelib,function(comscore){
						if(comscore)
						{
							NLComscoreTracker.initialize(config);
							if(config.playerId!=null)
								NLComscoreTracker.createVideoTracker(config);
						}
					});
				}
				else
				{
					var comscorelib = ["nlbase/comscore", "nlbase/streamsense.min"];
					if(config.comscore[4]!=null)
					{
						var version = config.comscore[4];
						if(version!=null && version.length > 0 && version == 'v2')
						{
							comscorelib = [];
							comscorelib.push("nlbase/nlcomscore2");
							comscorelib.push("nlbase/streamsense2.min");
						}
					}
					NL.require(comscorelib,function(comscore){
						if(comscore)
						{
							NLComscoreTracker.initialize(config);
							if(config.playerId!=null)
								NLComscoreTracker.createVideoTracker(config);
						}
					});
				}
			}
			if(config.externalTrackCallback!=null)
			{
				NL.require(["nlbase/externaltracker"],function(external){
					if(external)
					{
						NLExternalTracker.initialize(config);
						if(config.playerId!=null)
							NLExternalTracker.createVideoTracker(config);
					}
				});
			}
			if(config.nielsen!=null)
			{
				if(!Array.isArray(config.nielsen))
				{
					NL.require(["nlbase/nlnielsen2"],function(nielsen){
						if(nielsen)
						{
							NLNielsenTracker.initialize(config);
							if(config.playerId!=null)
								NLNielsenTracker.createVideoTracker(config);
						}
					});
				}
				else
				{
					var nielsenlib = [];
					var prefix = "http://secure-";
					if(window.location.protocol == "https:")
						prefix = "https://secure-";
					if(config.nielsen[3])
						nielsenlib.push(prefix+config.nielsen[1]+".imrworldwide.com/novms/js/2/ggcmb500.js");
					if(config.nielsen[4])
						nielsenlib.push(prefix+config.nielsen[1]+".imrworldwide.com/novms/js/2/ggcmb510.js");

					NL.require(nielsenlib,function(){
						NL.require(["nlbase/nlnielsen"],function(nielsen){
							if(nielsen)
							{
								NLNielsenTracker.initialize(config);
								if(config.playerId!=null)
									NLNielsenTracker.createVideoTracker(config);
							}
						});
					});
				}
			}
			if(config.heartbeat!=null)
			{
				NL.require(["nlbase/nladobeheartbeat", "nlbase/VideoHeartbeat.min"],function(heartbeat){
					if(heartbeat)
					{
						NLAdobeHeartbeatTracker.initialize(config);
						if(config.playerId!=null)
							NLAdobeHeartbeatTracker.createVideoTracker(config);
					}
				});
			}

			if(config.personalization!=null)
			{
				NL.require(["nlbase/nlplayerps"],function(ps){
					if(ps)
					{
						NLPSTracker.initialize(config);
						if(config.playerId!=null)
							NLPSTracker.createVideoTracker(config);
					}
				});
			}

			if(config.yospace!=null)
			{
				NL.require(["nlbase/nlys"],function(ys){
					if(ys)
					{
						NLYSTracker.initialize(config);
						if(config.playerId!=null)
							NLYSTracker.createVideoTracker(config);
					}
				});
			}
		}
	}

	this.reInitialize = function(config)
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.reInit(config);
		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.reInit(config);
	};

	this.destroy = function()
	{
		if(typeof NLGATracker != 'undefined' && NLGATracker.reset != null)
		{
			NLGATracker.reset(this.config);
		}
		if(typeof NLQosTracker != 'undefined' && NLQosTracker.reset != null)
		{
			NLQosTracker.reset(this.config);
		}
		if(typeof NLComscoreTracker != 'undefined' && NLComscoreTracker.reset != null)
		{
			NLComscoreTracker.reset(this.config);
		}
		if(typeof NLExternalTracker != 'undefined' && NLExternalTracker.reset != null)
		{
			NLExternalTracker.reset(this.config);
		}
		if(typeof NLNielsenTracker != 'undefined' && NLNielsenTracker.reset != null)
		{
			NLNielsenTracker.reset(this.config);
		}
		if(typeof NLAdobeHeartbeatTracker != 'undefined' && NLAdobeHeartbeatTracker.reset != null)
		{
			NLAdobeHeartbeatTracker.reset(this.config);
		}
		if(typeof NLPSTracker != 'undefined' && NLPSTracker.reset != null)
		{
			NLPSTracker.reset(this.config);
		}
		if(typeof NLYSTracker != 'undefined' && NLYSTracker.reset != null)
		{
			NLYSTracker.reset(this.config);
		}
	}

	/*
		Common initialization code for CatchMedia
		To handle initialization after QoS and indenpendently
	*/
	function nlInitializeCatchMediaTracker(config)
	{
		if(window.NLCONFIGS_CATCHMEDIA!=null || config.catchmedia!=null)
		{
			if(window.NLCONFIGS_CATCHMEDIA!=null && config.catchmedia==null)
				config.catchmedia = window.NLCONFIGS_CATCHMEDIA;

			if(config.catchmedia!=null)
			{
				NL.require(["nlbase/nlcatchmedia","CMSDK"],function(cm, sdk){
					if(cm, sdk)
					{
						NLCatchMediaTracker.initialize(config, sdk);
						if(config.playerId!=null)
							NLCatchMediaTracker.createVideoTracker(config);
					}
				});
			}
		}
	}

	var trackerInitCounter = 0;
	this.trackPage = function(pageName)
	{
		if(NLTracker.initialized)
		{
			if(NLTracker.config.gaa!=null)
			{
				if(typeof NLGATracker != 'undefined')
					NLGATracker.trackPage(pageName);
				else
				{
					NL.require(['nlbase/nlga'], function (ga) {
						NLGATracker.trackPage(pageName);
					});
				}
			}

			if(NLTracker.config.locQos!=null && NLTracker.config.locQos.toString().length>0)
			{
				NL.require(["nlbase/nlqos", "nlbase/nltrack.min"],function(qos){
							NLQosTracker.trackPage(pageName);
							trackPageCatchMedia();
						},
						function(error){
							trackPageCatchMedia();
						});
			}
			else
			{
				trackPageCatchMedia();
			}
		}
		else
		{
			if((trackerInitCounter++)<100)
				setTimeout(function(){NLTracker.trackPage(pageName)},100);
			else
				setTimeout(function(){NLTracker.trackPage(pageName)},5000);
		}

		function trackPageCatchMedia()
		{
			if(window.NLCONFIGS_CATCHMEDIA!=null || (NLTracker.config!=null && NLTracker.config.catchmedia!=null))
			{
				if(window.NLCONFIGS_CATCHMEDIA!=null && NLTracker.config.catchmedia==null)
					NLTracker.config.catchmedia = window.NLCONFIGS_CATCHMEDIA;
				if(NLTracker.config.catchmedia!=null)
				{
					NL.require(["nlbase/nlcatchmedia", "CMSDK"], function(cm, sdk){
						NLCatchMediaTracker.trackPage(pageName);
					});
				}
			}
		}
	};

	this.trackLogin = function(userId, userType, tuid, tlid)
	{
		if(typeof NLGATracker != 'undefined' && tuid!=null)
			NLGATracker.trackLogin(tuid, userType);

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackLogin(userId, userType, tlid);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackLogin(userId, userType, tlid);
	};

	this.trackMVPDLogin = function(mvpdId, mvpdUserId, userType)
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.trackMVPDLogin(mvpdId, mvpdUserId, userType);

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackMVPDLogin(mvpdId, mvpdUserId, userType);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackMVPDLogin(mvpdId, mvpdUserId, userType);
	};

	this.trackLogout = function()
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.trackLogout();

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackLogout();

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackLogout();
	};

	this.trackRegistration = function(username)
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.trackRegistration();

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackRegistration(username);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackRegistration();
	};

	this.trackPurchaseSelection = function(packageInfo)
	{
		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackPurchaseSelection(packageInfo);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackPurchaseSelection(packageInfo);
	};

	this.trackPurchaseBilling = function(packageInfo)
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.trackPurchaseBilling();

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackPurchaseBilling(packageInfo);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackPurchaseBilling(packageInfo);
	};

	this.trackPurchaseConfirmation = function(packageInfo)
	{
		if(typeof NLGATracker != 'undefined')
			NLGATracker.trackPurchaseConfirmation(packageInfo);

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackPurchaseConfirmation(packageInfo);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackPurchaseConfirmation(packageInfo);
	};

	this.trackVideoClick = function(trackInfo)
	{
		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackVideoClick(trackInfo);
	};

	this.trackError = function(err, info)
	{
		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackError(err);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackError(err, info);
	};

	this.updatePlayheadTime = function(id, time, type)
	{
		if(typeof NLNielsenTracker != 'undefined')
			NLNielsenTracker.updatePlayheadTime(id, time, type);
	};

	this.trackAction = function(action, info)
	{
		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackAction(action, info);
	};

	this.trackCustomAppEvent = function(eventName, info)
	{
		if(typeof NLGATracker != 'undefined')
		{
			if(eventName == "search" && info!=null && info.keyword!=null)
				NLGATracker.trackPage("/search?param="+info.keyword.toString());
		}

		if(typeof NLQosTracker != 'undefined')
			NLQosTracker.trackCustomAppEvent(eventName, info);

		if(typeof NLCatchMediaTracker != 'undefined')
			NLCatchMediaTracker.trackCustomAppEvent(eventName, info);
	};

	this.createVideoTracker = function(config)
	{
		if(config.gaa!=null)
		{
			var hasGA = false;
			if(isFlash(config))
			{
				if(config.gaa!=null && (config.comscore!=null || config.externalTrackCallback!=null || config.nielsen!=null || config.heartbeat!=null||config.personalization!=null))
					hasGA = true;
			}
			else if(config.gaa!=null)
				hasGA = true;

			if(hasGA)
			{
				if(typeof NLGATracker!= 'undefined')
					NLGATracker.createVideoTracker(config);
				else
				{
					NL.require(["nlbase/nlga"],function(ga){
						if(ga)
							NLGATracker.createVideoTracker(config);
					});
				}
			}
		}

		if(config.locQos!=null && config.locQos.toString().length>0 && !isFlash(config))
		{
			if(typeof NLQosTracker!= 'undefined')
				NLQosTracker.createVideoTracker(config);
			else
			{
				NL.require(["nlbase/nlqos", "nlbase/nltrack.min"],function(qos){
					if(qos)
						NLQosTracker.createVideoTracker(config);
				});
			}
		}

		if(config.comscore!=null)
		{
			if(typeof NLComscoreTracker!= 'undefined')
				NLComscoreTracker.createVideoTracker(config);
			else
			{
				if(!Array.isArray(config.comscore))
				{
					var comscorelib = ["nlbase/nlcomscore3"];
					NL.require(comscorelib,function(comscore){
						if(comscore)
						{
							NLComscoreTracker.initialize(config);
							if(config.playerId!=null)
								NLComscoreTracker.createVideoTracker(config);
						}
					});
				}
				else
				{
					var comscorelib = ["nlbase/comscore", "nlbase/streamsense.min"];
					if(config.comscore[4]!=null)
					{
						var version = config.comscore[4];
						if(version!=null && version.length > 0 && version == 'v2')
						{
							comscorelib = [];
							comscorelib.push("nlbase/nlcomscore2");
							comscorelib.push("nlbase/streamsense2.min");
						}
					}
					NL.require(comscorelib,function(comscore){
						if(comscore)
						{
							NLComscoreTracker.initialize(config);
							if(config.playerId!=null)
								NLComscoreTracker.createVideoTracker(config);
						}
					});
				}
			}
		}

		if(config.externalTrackCallback!=null)
		{
			if(typeof NLExternalTracker!= 'undefined')
				NLExternalTracker.createVideoTracker(config);
			else
			{
				NL.require(["nlbase/externaltracker"],function(external){
					if(external)
						NLExternalTracker.createVideoTracker(config);
				});
			}
		}

		if(config.nielsen!=null)
		{
			if(typeof NLNielsenTracker!= 'undefined')
				NLNielsenTracker.createVideoTracker(config);
			else
			{
				if(!Array.isArray(config.nielsen))
				{
					NL.require(["nlbase/nlnielsen2"],function(nielsen){
						if(nielsen)
						{
							if(config.playerId!=null)
								NLNielsenTracker.createVideoTracker(config);
						}
					});
				}
				else
				{
					var nielsenlib = [];
					var prefix = "http://secure-";
					if(window.location.protocol == "https:")
						prefix = "https://secure-";
					if(config.nielsen[3])
						nielsenlib.push(prefix+config.nielsen[1]+".imrworldwide.com/novms/js/2/ggcmb500.js");
					if(config.nielsen[4])
						nielsenlib.push(prefix+config.nielsen[1]+".imrworldwide.com/novms/js/2/ggcmb510.js");

					NL.require(nielsenlib,function(){
						NL.require(["nlbase/nlnielsen"],function(nielsen){
							if(nielsen)
								NLNielsenTracker.createVideoTracker(config);
						});
					});
				}
			}
		}

		if(config.heartbeat!=null)
		{
			if(typeof NLAdobeHeartbeatTracker!= 'undefined')
				NLAdobeHeartbeatTracker.createVideoTracker(config);
			else
			{
				NL.require(["nlbase/nladobeheartbeat", "nlbase/VideoHeartbeat.min"],function(heartbeat){
					if(heartbeat)
						NLAdobeHeartbeatTracker.createVideoTracker(config);
				});
			}
		}

		if(config.personalization!=null)
		{
			if(typeof NLPSTracker!= 'undefined')
				NLPSTracker.createVideoTracker(config);
			else
			{
				NL.require(["nlbase/nlplayerps"],function(ps)
				{
					if(ps)
						NLPSTracker.createVideoTracker(config);
				});
			}
		}

		if(config.yospace!=null)
		{
			if(typeof NLYSTracker!= 'undefined')
				NLYSTracker.createVideoTracker(config);
			else
			{
				NL.require(["nlbase/nlys"],function(ys)
				{
					if(ys)
						NLYSTracker.createVideoTracker(config);
				});
			}
		}
	};

	this.trackEvent = function(htmlid, action, data)
	{
		data.htmlid = htmlid;
		if(data.video.id!=null)
		{
			switch(action)
			{
				case "videostart":
					nlTriggerEvent('nlvideostart','playerEvent',data);
					break;

				case "videocomplete":
					nlTriggerEvent('nlvideocomplete','playerEvent',data);
					break;

				case "videopercent":
					nlTriggerEvent('nlvideopercent','playerEvent',data);
					break;

				case "videoduration":
					nlTriggerEvent('nlvideoduration','playerEvent',data);
					break;

				case "videostate":
					nlTriggerEvent('nlvideostate','playerEvent',data);
					break;

				case "videostatus":
					nlTriggerEvent('nlvideostatus','playerEvent',data);
					break;

				case "videoerror":
					nlTriggerEvent('nlvideoerror','playerEvent',data);
					break;

				case "adstart":
					nlTriggerEvent('nladstart','playerEvent',data);
					break;

				case "adpause":
					nlTriggerEvent('nladpause','playerEvent',data);
					break;

				case "adresume":
					nlTriggerEvent('nladresume','playerEvent',data);
					break;

				case "adcomplete":
					nlTriggerEvent('nladcomplete','playerEvent',data);
					break;

				case "customevent":
					nlTriggerEvent('nlcustomevent','playerEvent',data);
					break;

				case "streamrating":
					nlTriggerEvent('nlstreamrating','playerEvent',data);
			}
		}
	};

	function nlTriggerEvent(eventName,eventType,data)
	{
		var element = null;
		if(data.htmlid.indexOf(':')>0)
		{
			var arr = data.htmlid.split(':');
			element = document.getElementById(arr[0]);
		}
		else
		{
			element = document.getElementById(data.htmlid);
		}
		if(element && document.createEvent)
		{
			var event = document.createEvent("CustomEvent");
			event.initCustomEvent(eventName, true, true,{'data':data});
			event.eventName = eventName;

			try
			{
				element.dispatchEvent(event);
			}
			catch(err){};
		}
	}

	function nlLoadScript(src)
	{
		var script = document.createElement("script");
		script.type = "text/javascript";
		script.src = src;
		var stag = document.getElementsByTagName("script")[0];
		stag.parentNode.insertBefore(script, stag);
	}

	function isFlash(config)
	{
		var isFlash = false;
		if(config.noFlash)
		{
			isFlash = false;
		}
		else if(window.swfobject!=null)
		{
			var pv = swfobject.getFlashPlayerVersion();
			if((pv!=null && pv.major==0))
				isFlash = false;
			else
				isFlash = true;
		}
		return isFlash;
	}
}
var NLTracker = new NLTracker();
