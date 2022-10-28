"use strict";(self.webpackChunkcontrol_wrapper_docs=self.webpackChunkcontrol_wrapper_docs||[]).push([[576],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>c});var r=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var l=r.createContext({}),d=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},p=function(e){var t=d(e.components);return r.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,i=e.mdxType,a=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),m=d(n),c=i,k=m["".concat(l,".").concat(c)]||m[c]||u[c]||a;return n?r.createElement(k,o(o({ref:t},p),{},{components:n})):r.createElement(k,o({ref:t},p))}));function c(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var a=n.length,o=new Array(a);o[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:i,o[1]=s;for(var d=2;d<a;d++)o[d]=n[d];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},4089:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>a,metadata:()=>s,toc:()=>d});var r=n(7462),i=(n(7294),n(3905));const a={sidebar_position:1},o="Users",s={unversionedId:"development/users",id:"development/users",title:"Users",description:"Listed below are all the user methods, along with their parameters, filters, and includes.",source:"@site/docs/development/users.md",sourceDirName:"development",slug:"/development/users",permalink:"/Control-Wrapper/docs/development/users",draft:!1,editUrl:"https://github.com/Ferks-FK/Control-Wrapper/tree/docs/docs/development/users.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Methods",permalink:"/Control-Wrapper/docs/category/methods"},next:{title:"Servers",permalink:"/Control-Wrapper/docs/development/servers"}},l={},d=[{value:"Create User",id:"create-user",level:2},{value:"List Users",id:"list-users",level:2},{value:"User Details",id:"user-details",level:2},{value:"Update User",id:"update-user",level:2},{value:"Suspend User",id:"suspend-user",level:2},{value:"Unsuspend User",id:"unsuspend-user",level:2},{value:"Increment User",id:"increment-user",level:2},{value:"Decrement User",id:"decrement-user",level:2},{value:"Delete User",id:"delete-user",level:2}],p={toc:d};function u(e){let{components:t,...n}=e;return(0,i.kt)("wrapper",(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"users"},"Users"),(0,i.kt)("p",null,"Listed below are all the user methods, along with their parameters, filters, and includes.",(0,i.kt)("br",null),"\nAll parameters that contain (",(0,i.kt)("inlineCode",{parentName:"p"},"*"),") are required."),(0,i.kt)("h2",{id:"create-user"},"Create User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the new registered user.",(0,i.kt)("br",null),"\nIf any of the supplied parameters are in the wrong format or are missing, (with the exception of the password), an error will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"name: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The user name. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\nemail: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The user email. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\npassword: Optional","[",(0,i.kt)("inlineCode",{parentName:"p"},"str"),"]"," -> The user password. If a password is not supplied, a random one will be generated.")),(0,i.kt)("admonition",{type:"info"},(0,i.kt)("p",{parentName:"admonition"},"If a random password is generated, this method or the API will NOT return the password.\nIn this case, the user will need to reset their password on the website.")),(0,i.kt)("h2",{id:"list-users"},"List Users"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns all users registered in the system, or ",(0,i.kt)("inlineCode",{parentName:"p"},"None")," if a specific user is not found.",(0,i.kt)("br",null),"\nOptionally you can provide Filters and Includes for user query.")),(0,i.kt)("admonition",{title:"Filters & Includes",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"name: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The user name.",(0,i.kt)("br",null),"\nemail: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The user email.",(0,i.kt)("br",null),"\nserver_limit: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> Limit of user servers.",(0,i.kt)("br",null),"\npterodactyl_id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The Pterodactyl ID of the user.",(0,i.kt)("br",null),"\nrole: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The user role. Available Roles: ",(0,i.kt)("inlineCode",{parentName:"p"},"['admin', 'mod', 'client', 'member']"),".",(0,i.kt)("br",null),"\nsuspended: ",(0,i.kt)("inlineCode",{parentName:"p"},"bool")," -> Whether the user is suspended or not.",(0,i.kt)("br",null),"\nincludes: ",(0,i.kt)("inlineCode",{parentName:"p"},"list")," -> List of includes. Available Includes: ",(0,i.kt)("inlineCode",{parentName:"p"},"['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']"),".")),(0,i.kt)("h2",{id:"user-details"},"User Details"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns data for a specific user, or ",(0,i.kt)("inlineCode",{parentName:"p"},"None")," if the user is not found.",(0,i.kt)("br",null),"\nThis is useful for checking whether a user has verified his discord account.")),(0,i.kt)("admonition",{title:"Parameters & Includes",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\nincludes: ",(0,i.kt)("inlineCode",{parentName:"p"},"list")," -> List of includes. Available Includes: ",(0,i.kt)("inlineCode",{parentName:"p"},"['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']"),".")),(0,i.kt)("h2",{id:"update-user"},"Update User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict with the user updated data.",(0,i.kt)("br",null),"\nIf the ",(0,i.kt)("inlineCode",{parentName:"p"},"email")," is in the incorrect format, or the user ID does not exist, one will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\nname: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The new user name. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\nemail: ",(0,i.kt)("inlineCode",{parentName:"p"},"str")," -> The new email of the user. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\ncredits: Optional","[",(0,i.kt)("inlineCode",{parentName:"p"},"int"),"]"," -> The new user credits.",(0,i.kt)("br",null),"\nserver_limit: Optional","[",(0,i.kt)("inlineCode",{parentName:"p"},"int"),"]"," -> The amount of servers user can manage.",(0,i.kt)("br",null),"\nrole: Optional","[",(0,i.kt)("inlineCode",{parentName:"p"},"str"),"]"," -> The new user role. Valid Roles: ",(0,i.kt)("inlineCode",{parentName:"p"},"['admin', 'moderator', 'client', 'member']"),".")),(0,i.kt)("admonition",{type:"info"},(0,i.kt)("p",{parentName:"admonition"},"For some reason the API forces you to pass the user ",(0,i.kt)("inlineCode",{parentName:"p"},"name")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"email")," address in order to update it.")),(0,i.kt)("h2",{id:"suspend-user"},"Suspend User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the user who was suspended.",(0,i.kt)("br",null),"\nIf the user is already suspended, or, the user ID passed in does not exist, an error will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"))),(0,i.kt)("h2",{id:"unsuspend-user"},"Unsuspend User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the user who had his suspension revoked.",(0,i.kt)("br",null),"\nIf the user is not already suspended, or, the user ID passed in does not exist, an error will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"))),(0,i.kt)("h2",{id:"increment-user"},"Increment User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the user who had an increment added.",(0,i.kt)("br",null),"\nIf the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\ncredits: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The amount of credits that will be added to the user.",(0,i.kt)("br",null),"\nserver_limit: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The amount of server limit that will be added to the user.")),(0,i.kt)("admonition",{type:"info"},(0,i.kt)("p",{parentName:"admonition"},"This method will not overwrite the user's existing server credits or limits, instead the new value will be added to the old one.",(0,i.kt)("br",null),"\nThe ",(0,i.kt)("inlineCode",{parentName:"p"},"credits")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"server_limit")," parameters are not required simultaneously, but one of them must be supplied.")),(0,i.kt)("h2",{id:"decrement-user"},"Decrement User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the user who had an decrement added.",(0,i.kt)("br",null),"\nIf the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"),(0,i.kt)("br",null),"\ncredits: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The amount of credits that will be added to the user.",(0,i.kt)("br",null),"\nserver_limit: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The amount of server limit that will be added to the user.")),(0,i.kt)("admonition",{type:"info"},(0,i.kt)("p",{parentName:"admonition"},"This method will not overwrite the user's existing server credits or limits, instead the new value will be deducted from the old one.",(0,i.kt)("br",null),"\nThe ",(0,i.kt)("inlineCode",{parentName:"p"},"credits")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"server_limit")," parameters are not required simultaneously, but one of them must be supplied.")),(0,i.kt)("h2",{id:"delete-user"},"Delete User"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"Returns a dict of the user that was deleted.",(0,i.kt)("br",null),"\nIf the user ID does not exist, an error is returned.")),(0,i.kt)("admonition",{title:"Parameters",type:"tip"},(0,i.kt)("p",{parentName:"admonition"},"id: ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," -> The user ID. ",(0,i.kt)("inlineCode",{parentName:"p"},"*"))),(0,i.kt)("admonition",{type:"danger"},(0,i.kt)("p",{parentName:"admonition"},"Currently this endpoint will delete the user, even if they have servers associated with them, so use this with caution.")))}u.isMDXComponent=!0}}]);