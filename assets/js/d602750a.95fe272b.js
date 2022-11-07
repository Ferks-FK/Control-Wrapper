"use strict";(self.webpackChunkcontrol_wrapper_docs=self.webpackChunkcontrol_wrapper_docs||[]).push([[20],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>u});var i=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,i)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,i,o=function(e,t){if(null==e)return{};var n,i,o={},r=Object.keys(e);for(i=0;i<r.length;i++)n=r[i],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(i=0;i<r.length;i++)n=r[i],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var s=i.createContext({}),p=function(e){var t=i.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},c=function(e){var t=p(e.components);return i.createElement(s.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},m=i.forwardRef((function(e,t){var n=e.components,o=e.mdxType,r=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=p(n),u=o,f=m["".concat(s,".").concat(u)]||m[u]||d[u]||r;return n?i.createElement(f,a(a({ref:t},c),{},{components:n})):i.createElement(f,a({ref:t},c))}));function u(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=n.length,a=new Array(r);a[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:o,a[1]=l;for(var p=2;p<r;p++)a[p]=n[p];return i.createElement.apply(null,a)}return i.createElement.apply(null,n)}m.displayName="MDXCreateElement"},7799:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>a,default:()=>d,frontMatter:()=>r,metadata:()=>l,toc:()=>p});var i=n(7462),o=(n(7294),n(3905));const r={sidebar_position:4},a="Notifications",l={unversionedId:"development/notifications",id:"development/notifications",title:"Notifications",description:"Listed below are all the notification methods, along with their parameters, filters, and includes.",source:"@site/docs/development/notifications.md",sourceDirName:"development",slug:"/development/notifications",permalink:"/Control-Wrapper/docs/development/notifications",draft:!1,editUrl:"https://github.com/Ferks-FK/Control-Wrapper/tree/docs/docs/development/notifications.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Vouchers",permalink:"/Control-Wrapper/docs/development/vouchers"}},s={},p=[{value:"User Notifications",id:"user-notifications",level:2},{value:"Notification Details",id:"notification-details",level:2},{value:"Send Notification To All Users",id:"send-notification-to-all-users",level:2},{value:"Send Notification To Specific Users",id:"send-notification-to-specific-users",level:2},{value:"Delete All Notifications",id:"delete-all-notifications",level:2},{value:"Delete Notification",id:"delete-notification",level:2}],c={toc:p};function d(e){let{components:t,...n}=e;return(0,o.kt)("wrapper",(0,i.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"notifications"},"Notifications"),(0,o.kt)("p",null,"Listed below are all the notification methods, along with their parameters, filters, and includes.",(0,o.kt)("br",null),"\nAll parameters that contain (",(0,o.kt)("inlineCode",{parentName:"p"},"*"),") are required."),(0,o.kt)("h2",{id:"user-notifications"},"User Notifications"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns all notifications from the user, or ",(0,o.kt)("inlineCode",{parentName:"p"},"None")," if user has no messages.",(0,o.kt)("br",null),"\nIf the user ID does not exist, an error is returned.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"id: ",(0,o.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))),(0,o.kt)("h2",{id:"notification-details"},"Notification Details"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns a dict containing the notification information, or an error if the user ID or notification ID does not exist.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"id: ",(0,o.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\nnotification_id: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The notification ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))),(0,o.kt)("h2",{id:"send-notification-to-all-users"},"Send Notification To All Users"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns a dict containing the sent message informations.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"title: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The title of the message. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\ncontent: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The content of the message. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\nvia: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The way in which users will receive the message. Available Methods: ",(0,o.kt)("inlineCode",{parentName:"p"},"['mail', 'database']"),". ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))),(0,o.kt)("admonition",{type:"info"},(0,o.kt)("p",{parentName:"admonition"},"If the shipping method chosen is ",(0,o.kt)("inlineCode",{parentName:"p"},"mail"),", and it is not working correctly on your server, an error will be returned.")),(0,o.kt)("h2",{id:"send-notification-to-specific-users"},"Send Notification To Specific Users"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns a dict containing the sent message informations.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"title: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The title of the message. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\ncontent: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The content of the message. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\nusers: ",(0,o.kt)("inlineCode",{parentName:"p"},"list")," -> The user ID's that will receive this message. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\nvia: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The way in which users will receive the message. Available Methods: ",(0,o.kt)("inlineCode",{parentName:"p"},"['mail', 'database']"),". ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))),(0,o.kt)("admonition",{type:"info"},(0,o.kt)("p",{parentName:"admonition"},"If the shipping method chosen is ",(0,o.kt)("inlineCode",{parentName:"p"},"mail"),", and it is not working correctly on your server, an error will be returned.")),(0,o.kt)("h2",{id:"delete-all-notifications"},"Delete All Notifications"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns a dict containing the information of the user deleted messages.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"id: ",(0,o.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))),(0,o.kt)("h2",{id:"delete-notification"},"Delete Notification"),(0,o.kt)("blockquote",null,(0,o.kt)("p",{parentName:"blockquote"},"Returns a dict containing the information of the deleted message.")),(0,o.kt)("admonition",{title:"Parameters",type:"tip"},(0,o.kt)("p",{parentName:"admonition"},"id: ",(0,o.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"),(0,o.kt)("br",null),"\nnotification_id: ",(0,o.kt)("inlineCode",{parentName:"p"},"str")," -> The notification ID. ",(0,o.kt)("inlineCode",{parentName:"p"},"*"))))}d.isMDXComponent=!0}}]);