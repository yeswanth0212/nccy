<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1X8EZLdvAMo0N_A9rnAEp8RmI5FRs9A4A#scrollTo=xjmQv7dJuOif -->
<html lang="en" theme="light" class="cell-ui-refresh" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="yeswanth0212@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./AttendanceSystem_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-QqfebjEuIgnKX+GxU4cN+byIJWmt6PLd1Lhx1lDrZnC9qHnUqKxROgib38rfVJzS" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./AttendanceSystem_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-QqfebjEuIgnKX+GxU4cN+byIJWmt6PLd1Lhx1lDrZnC9qHnUqKxROgib38rfVJzS" nonce=""></script><script src="./AttendanceSystem_files/cb=gapi.loaded_1" nonce="" async=""></script><script type="text/javascript" async="" src="./AttendanceSystem_files/js" nonce=""></script><script src="./AttendanceSystem_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./AttendanceSystem_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>AttendanceSystem.py - Colab</title><link href="./AttendanceSystem_files/css2" rel="stylesheet"><link href="./AttendanceSystem_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_ub{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Ra{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none;user-select:none}a.gb_Ra:hover::after,a.gb_Ra:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Ra:hover,a.gb_Ra:focus{text-decoration:none}a.gb_Ra:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Sa{background-color:#4285f4;color:#fff}a.gb_Sa:active{background-color:#0043b2}.gb_Ta{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Ra,.gb_Sa,.gb_Ua,.gb_Va{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ua,.gb_Va{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua,#gb a.gb_Ua.gb_Ua,.gb_Va,#gb a.gb_Va{color:#666;cursor:default;text-decoration:none}.gb_Va{border:1px solid #4285f4;font-weight:bold;outline:none;background:-webkit-gradient(linear,left top,left bottom,from(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(to bottom,#4387fd,#4683ea)}#gb a.gb_Va{color:#fff}.gb_Va:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Va:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:-webkit-gradient(linear,left top,left bottom,from(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(to bottom,#3c7ae4,#3f76d3)}#gb .gb_Wa{background:#ffffff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Wa:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Wa:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Wa:active,#gb .gb_Wa:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Wa.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Wa.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Wa.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Wa.gb_H:active,#gb .gb_Wa.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_td{display:inline-block;padding:4px 4px 4px 4px;vertical-align:middle}.gb_ud .gb_R{bottom:-3px;right:-5px}.gb_td:first-child,#gbsfw:first-child+.gb_td{padding-left:0}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px}.gb_B,#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_vd,.gb_wd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:6.5px;top:37px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_wd{border-bottom-color:#ccc;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_wd{border-bottom-color:#ccc}.gb_ma{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-moz-user-select:text;-ms-user-select:text;-webkit-user-select:text}.gb_td.gb_8c .gb_vd,.gb_td.gb_8c .gb_wd,.gb_td.gb_8c .gb_ma,.gb_8c.gb_ma{display:block}.gb_td.gb_8c.gb_xd .gb_vd,.gb_td.gb_8c.gb_xd .gb_wd{display:none}.gb_yd{position:absolute;right:8px;top:62px;z-index:-1}.gb_lb .gb_vd,.gb_lb .gb_wd,.gb_lb .gb_ma{margin-top:-10px}.gb_td:first-child,#gbsfw:first-child+.gb_td{padding-left:4px}.gb_Ha.gb_zd .gb_td:first-child{padding-left:0}.gb_Ad{position:relative}.gb_gd .gb_Ad,.gb_Bd .gb_Ad{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Ha .gb_Cd:not(.gb_Ra):focus img{background-color:rgba(0,0,0,.2);outline:none;border-radius:50%}.gb_Dd button svg,.gb_B{border-radius:50%}.gb_Dd button:focus:not(:focus-visible) svg,.gb_Dd button:hover svg,.gb_Dd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_0c .gb_Dd.gb_Ed button:focus-visible svg,.gb_Dd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_0c .gb_Dd button:focus-visible svg,.gb_0c .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_0c .gb_Dd.gb_Ed button:focus-visible svg,.gb_Dd button:focus-visible svg,.gb_0c .gb_Dd button:focus-visible svg{outline:1px solid currentcolor}}.gb_0c .gb_Dd.gb_Ed button:focus svg,.gb_0c .gb_Dd.gb_Ed button:focus:hover svg,.gb_Dd button:focus svg,.gb_Dd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_0c .gb_Dd.gb_Ed button:active svg,.gb_Dd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_0c .gb_Dd.gb_Ed button:hover svg,.gb_Dd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Xa .gb_B.gb_0a:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_0c .gb_Dd button:hover svg,.gb_0c .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_0c .gb_Dd button:focus svg,.gb_0c .gb_Dd button:focus:hover svg,.gb_0c .gb_B:focus,.gb_0c .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_0c .gb_Dd button:active svg,.gb_0c .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_0c .gb_B[aria-expanded=true],.gb_0c .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_0c .gb_B[aria-expanded=true] .gb_F{fill:#ffffff;opacity:1}.gb_td{padding:4px}.gb_Ha.gb_zd .gb_td{padding:4px 2px}.gb_Ha.gb_zd .gb_z.gb_td{padding-left:6px}.gb_ma{z-index:991;line-height:normal}.gb_ma.gb_Fd{left:0;right:auto}@media (max-width:350px){.gb_ma.gb_Fd{left:0}}.gb_Hd .gb_ma{top:56px}.gb_S{display:none!important}.gb_fb{visibility:hidden}.gb_J .gb_B{background-position:-64px -29px;opacity:.55}.gb_la .gb_J .gb_B{background-position:-64px -29px}.gb_2 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_Id:not(.gb_Jd) .gb_J{display:none;visibility:hidden}}.gb_R{display:none}.gb_nd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_nd.gb_od{color:#3c4043}.gb_Ha.gb_oc .gb_nd{margin-bottom:0}.gb_pd.gb_qd .gb_nd{padding-left:4px}.gb_Ha.gb_oc .gb_rd{position:relative;top:-2px}.gb_sd{display:none}.gb_Ha{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow .25s;transition:box-shadow .25s}.gb_Ha.gb_7c{min-width:120px}.gb_Ha.gb_Pd .gb_Qd{display:none}.gb_Ha.gb_Pd .gb_Id{height:56px}header.gb_Ha{display:block}.gb_Ha svg{fill:currentColor}.gb_Rd{position:fixed;top:0;width:100%}.gb_Sd{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Td{height:64px}.gb_Id{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ha:not(.gb_oc) .gb_Id{padding:8px}.gb_Ha.gb_Vd .gb_Id{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha .gb_Id.gb_Jd.gb_Wd{min-width:0}.gb_Ha.gb_oc .gb_Id{padding:4px;padding-left:8px;min-width:0}.gb_Qd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_Xd>.gb_Qd{display:table-cell;width:100%}.gb_pd{padding-right:30px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha.gb_oc .gb_pd{padding-right:14px}.gb_Zd{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_Zd>:only-child{display:inline-block}.gb_0d.gb_hd{padding-left:4px}.gb_0d.gb_1d,.gb_Ha.gb_Vd .gb_0d,.gb_Ha.gb_oc:not(.gb_Bd) .gb_0d{padding-left:0}.gb_Ha.gb_oc .gb_0d.gb_1d{padding-right:0}.gb_Ha.gb_oc .gb_0d.gb_1d .gb_Xa{margin-left:10px}.gb_hd{display:inline}.gb_Ha.gb_bd .gb_0d.gb_2d,.gb_Ha.gb_Bd .gb_0d.gb_2d{padding-left:2px}.gb_nd{display:inline-block}.gb_0d{box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Bd{height:48px}.gb_Ha.gb_Bd{min-width:auto}.gb_Bd .gb_0d{float:right;padding-left:32px}.gb_Bd .gb_0d.gb_3d{padding-left:0}.gb_4d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_Ld{-webkit-transition:background-color .4s;transition:background-color .4s}.gb_7d{color:black}.gb_0c{color:white}.gb_Ha a,.gb_4c a{color:inherit}.gb_ca{color:rgba(0,0,0,.87)}.gb_Ha svg,.gb_4c svg,.gb_pd .gb_Od,.gb_gd .gb_Od{color:#5f6368;opacity:1}.gb_0c svg,.gb_4c.gb_9c svg{color:rgba(255,255,255,.87)}.gb_0c .gb_pd .gb_Od,.gb_0c .gb_pd .gb_Zc,.gb_0c .gb_pd .gb_rd,.gb_4c.gb_9c .gb_Od{color:rgba(255,255,255,.87)}.gb_0c .gb_pd .gb_Xc:not(.gb_8d){opacity:.87}.gb_od{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_0c .gb_od,.gb_7d .gb_od{opacity:1}.gb_5d{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_Z,span.gb_Z{color:rgba(0,0,0,.87);text-decoration:none}.gb_0c a.gb_Z,.gb_0c span.gb_Z{color:white}a.gb_Z:focus{outline-offset:2px}a.gb_Z:hover{text-decoration:underline}.gb_0{display:inline-block;padding-left:15px}.gb_0 .gb_Z{display:inline-block;line-height:24px;vertical-align:middle}.gb_Md{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Ha.gb_Bd .gb_Md{margin-left:8px}#gb a.gb_Va.gb_Md{cursor:pointer}.gb_Va.gb_Md:hover{background:#1b66c9;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Va.gb_Md:focus,.gb_Va.gb_Md:hover:focus{background:#1c5fba;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Va.gb_Md:active{background:#1b63c1;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Md{background:#1a73e8;border:1px solid transparent}.gb_Ha.gb_oc .gb_Md{padding:9px 15px;min-width:80px}.gb_6d{text-align:left}#gb .gb_0c a.gb_Md:not(.gb_H),#gb.gb_0c a.gb_Md{background:#fff;border-color:#dadce0;box-shadow:none;color:#1a73e8}#gb a.gb_Va.gb_H.gb_Md{background:#8ab4f8;border:1px solid transparent;box-shadow:none;color:#202124}#gb .gb_0c a.gb_Md:hover:not(.gb_H),#gb.gb_0c a.gb_Md:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Va.gb_H.gb_Md:hover{background:#93baf9;border-color:transparent;box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_0c a.gb_Md:focus:not(.gb_H),#gb .gb_0c a.gb_Md:focus:hover:not(.gb_H),#gb.gb_0c a.gb_Md:focus:not(.gb_H),#gb.gb_0c a.gb_Md:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Va.gb_H.gb_Md:focus,#gb a.gb_Va.gb_H.gb_Md:focus:hover{background:#a6c6fa;border-color:transparent;box-shadow:none}#gb .gb_0c a.gb_Md:active:not(.gb_H),#gb.gb_0c a.gb_Md:active{background:#ecf3fe}#gb a.gb_Va.gb_H.gb_Md:active{background:#a1c3f9;box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_Id .gb_J{display:none;visibility:hidden}}.gb_Xa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Xa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_4a{display:inherit}.gb_Xa.gb_H .gb_4a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Xa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Xa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Xa:focus-visible,.gb_Xa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Xa.gb_H:focus-visible,.gb_Xa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Xa.gb_H:active,.gb_Xa.gb_8c.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_5a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Xa.gb_H .gb_5a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_5a.gb_6a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_5a.gb_6a .gb_Vc{vertical-align:middle}.gb_Ha:not(.gb_oc) .gb_Xa{margin-left:10px;margin-right:4px}.gb_9d{max-height:32px;width:78px}.gb_Xa.gb_H .gb_9d{max-height:26px;width:72px}.gb_Q{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_gb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_gb.gb_Q{height:30px;width:30px}.gb_gb.gb_Q:hover,.gb_gb.gb_Q:active{-webkit-box-shadow:none;box-shadow:none}.gb_hb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_ib{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_Q::before,.gb_jb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_4 .gb_jb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_Q:hover,.gb_Q:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Q:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Q:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_kb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_kb{width:auto}.gb_kb:hover,.gb_kb:focus{opacity:.85}.gb_lb .gb_kb,.gb_lb .gb_mb{line-height:26px}#gb#gb.gb_lb a.gb_kb,.gb_lb .gb_mb{font-size:11px;height:auto}.gb_nb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_0a:hover .gb_nb{opacity:.85}.gb_Xa>.gb_z{padding:3px 3px 3px 4px}.gb_ob.gb_fb{color:#fff}.gb_2 .gb_kb,.gb_2 .gb_nb{opacity:1}#gb#gb.gb_2.gb_2 a.gb_kb,#gb#gb .gb_2.gb_2 a.gb_kb{color:#fff}.gb_2.gb_2 .gb_nb{border-top-color:#fff;opacity:1}.gb_la .gb_Q:hover,.gb_2 .gb_Q:hover,.gb_la .gb_Q:focus,.gb_2 .gb_Q:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_pb .gb_z,.gb_qb .gb_z{position:absolute;right:1px}.gb_z.gb_1,.gb_rb.gb_1,.gb_0a.gb_1{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_sb.gb_tb .gb_kb{width:30px!important}.gb_P{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_ub .gb_P,.gb_vb .gb_P{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_T{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.InInzjbyX2s.2019.O","co.in","en","425",0,[4,2,"","","","809810803","0"],null,"tInaaMsk8Z-nzg_xw-y5Bg",null,0,"og.qtm.pfog22aEnAs.L.W.O","AA2YrTthnASDYd0N4gbIL91FDhrpfXlj5w","AA2YrTskOaSug7MVZwlus97OpUaPcMM3bw","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","yeswanth0212@gmail.com","","AFD17dPms4eheAj7p4hQeiKRDKkK5aupRMBx8RX0CT9G2RKrfvaFih921HnxuKWVeXXptwWQcb-VTLY4DTVJ5vmFCAP6U1AIsg",0,0,null,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.GJa4oir6WlA.O/d=1/rs=AHpOoo-oT18V72om9ubISB9Na8GvbQT5cg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250803.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","809810803.0",8,null,1,0,null,null,null,null,"3700949,102911461,102911463,105109531,105109534",null,null,null,"tInaaMsk8Z-nzg_xw-y5Bg",0,0,0,null,2,5,"nn",167,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.InInzjbyX2s.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTthnASDYd0N4gbIL91FDhrpfXlj5w"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.pfog22aEnAs.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTskOaSug7MVZwlus97OpUaPcMM3bw"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,1,0],0,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/\u0026timeStmp=1759152564\u0026secTok=.AG5fkS8Da0GocT8nTllgufI2lbW4geCJtg\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"8559284470",3,1,0],0,null,null,null,1,0,"yeswanth0212@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,$a,cb,eb,jb,fb,lb,rb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.yk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.fa[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Qa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Ra=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Sa=function(a){return a==null||typeof a==="string"?a:void 0};_.Va=function(a,b,c){if(a!=null&&a[_.Ta]===_.Ua)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Ya=function(a){const b=_.Wa(_.Xa);return b?a[b]:void 0};$a=function(a,b){b<100||_.Ja(Za,1)};
cb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Wa(_.Xa),g;!e&&f&&(g=a[f])&&g.xd($a);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=ab)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const D=r-p;var q=void 0;((q=b)!=null?q:b={})[D]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let D;if(m&&!Number.isNaN(h)&&(D=h+p)<g)f[D]=q;else{let Q;((Q=b)!=null?Q:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Wa(_.Xa)&&(a=_.Ya(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(f[_.Xa]=a.i());return f};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:cb(a,b,eb)}if(a!=null&&a[_.Ta]===_.Ua)return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Fa||b[hb]!==ib?Fa:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.fa;return cb(a,a[_.v]|0,eb)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(kb&&1&e)throw Error("m");2048&e&&!(2&e)&&lb();if(e&256)throw Error("n");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<
g)c[f+b]=k[h],delete k[h];else break;e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){if(kb)throw Error("p");_.Ja(nb,5)};
rb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ta]===_.Ua)return b=a.fa,c=b[_.v]|0,_.Ea(a,c)?a:_.pb(a,b,c)?_.qb(a,b):_.ob(b,c);if("function"==typeof _.gb&&a instanceof _.gb)return a};_.qb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=cb(a,b,rb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};_.tb=function(a){const b=a.fa,c=b[_.v]|0;return _.Ea(a,c)?_.pb(a,b,c)?_.qb(a,b,!0):new a.constructor(_.ob(b,c,!1)):a};_.ub=function(a){if(a.j!==Da)return!1;var b=a.fa;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.fa=b;a.j=void 0;a.o=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Ea(a,a.fa[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.pb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.xb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.zb=function(a,b,c,d,e){let f=!1;d=_.yb(a,d,e,g=>{const h=_.Va(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.wb(a,b),d};_.Ab=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};Db=Object.defineProperty;
Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};Gb("globalThis",function(a){return a||Fb});
Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});Gb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Gb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Wa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.mk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>15&1),Qb=!!(Kb[0]&1024),Rb=!!(Kb[0]>>16&1),Sb=!!(Kb[0]&128);var Tb=Jb(1,!0),na=Pb?Rb:Jb(610401301,!1),kb=Pb?Qb||!Sb:Jb(748402147,Tb);_.Ub=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Xb,Vb,Yb,Wb;_.db=_.ba(a=>fa?a>=Vb&&a<=Wb:a[0]==="-"?ja(a,Xb):ja(a,Yb));Xb=Number.MIN_SAFE_INTEGER.toString();Vb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Yb=Number.MAX_SAFE_INTEGER.toString();Wb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Zb=typeof TextDecoder!=="undefined";_.$b=typeof TextEncoder!=="undefined";var oa,ac=_.t.navigator;oa=ac?ac.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.bc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.cc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.dc=function(a){_.dc[" "](a);return a};_.dc[" "]=function(){};var rc;_.ec=_.ra();_.fc=_.sa();_.hc=_.u("Edge");_.ic=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.jc=_.ma()&&!_.u("Edge");_.kc=_.za();_.lc=wa()?oa.platform==="Windows":_.u("Windows");_.mc=wa()?oa.platform==="Android":_.u("Android");_.nc=xa();_.oc=_.u("iPad");_.pc=_.u("iPod");_.qc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.ic)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.hc)return/Edge\/([\d\.]+)/.exec(c);if(_.fc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.jc)return/WebKit\/(\S+)/.exec(c);if(_.ec)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.fc){var sc;const c=_.t.document;sc=c?c.documentMode:void 0;if(sc!=null&&sc>parseFloat(a)){rc=String(sc);break a}}rc=a}_.tc=rc;_.uc=_.ta();_.vc=xa()||_.u("iPod");_.wc=_.u("iPad");_.xc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.yc=ua();_.zc=_.va()&&!_.ya();var Za,nb,hb;_.Xa=_.Ca();_.Ac=_.Ca();Za=_.Ca();_.Bc=_.Ca();nb=_.Ca();_.Ta=_.Ca("m_m",!0);hb=_.Ca();_.Cc=_.Ca();var Ec;_.v=_.Ca("jas",!0);Ec=[];Ec[_.v]=7;_.Dc=Object.freeze(Ec);var Da;_.Ua={};Da={};_.Fc=Object.freeze({});var ib={};var Ia=void 0;_.Gc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Hc=Number.isSafeInteger;_.Na=Number.isFinite;_.Ic=Math.trunc;var ab;_.Jc=_.ia(0);_.Kc={};_.Lc=function(a,b,c,d,e){b=_.yb(a.fa,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.yb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Mc=function(a,b,c,d){_.vb(a);const e=a.fa;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.fa,f=e[_.v]|0;b=_.zb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.fa,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.E=function(a,b,c){c==null&&(c=void 0);_.Mc(a,b,c);c&&!_.Ea(c)&&_.wb(a.fa);return a};_.Nc=function(a,b,c,d){return _.Pa(_.Lc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Lc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Sa(_.Lc(a,b,d)))!=null?e:c};
_.I=function(a,b,c){return _.Sa(_.Lc(a,b,c,_.Kc))};_.J=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Mc(a,b,c==null?c:_.Qa(c))};_.L=function(a,b,c,d){return _.Mc(a,b,_.Ra(c),d)};_.N=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.Oa(c),d)};_.O=class{constructor(a,b,c){this.fa=_.mb(a,b,c)}toJSON(){return jb(this)}wa(a){return JSON.stringify(jb(this,a))}};_.O.prototype[_.Ta]=_.Ua;_.O.prototype.toString=function(){return this.fa.toString()};_.Oc=_.Ab();_.Qc=_.Ab();_.Rc=_.Ab();_.Sc=Symbol();var Tc=class extends _.O{constructor(a){super(a)}};_.Uc=class extends _.O{constructor(a){super(a)}D(a){return _.K(this,3,a)}};_.Vc=class extends _.O{constructor(a){super(a)}};_.P=function(){this.qa=this.qa;this.Y=this.Y};_.P.prototype.qa=!1;_.P.prototype.isDisposed=function(){return this.qa};_.P.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.P.prototype[Symbol.dispose]=function(){this.dispose()};_.P.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Wc=class extends _.P{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}ub(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].ub(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Yc=class extends _.P{constructor(){var a=_.Xc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Zc=class extends _.O{constructor(a){super(a)}};var $c=class extends _.O{constructor(a){super(a)}};var cd;_.ad=function(a,b,c=98,d=new _.Uc){if(a.i){const e=new Tc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.N(e,5,1);_.E(d,40,e);a.i.log(c,d)}};cd=class{constructor(){var a=bd;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Uc){_.ad(this,a,98,c)}};var dd,ed;dd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.bc(c,b,a)}catch(d){console.error(d)}}}};_.fd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new ed(a,b,c));dd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;dd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;dd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
ed=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.gd=a=>{var b="rc";if(a.rc&&a.hasOwnProperty(b))return a.rc;b=new a;return a.rc=b};_.R=class{constructor(){this.v=new _.fd;this.i=new _.fd;this.D=new _.fd;this.B=new _.fd;this.C=new _.fd;this.A=new _.fd;this.o=new _.fd;this.j=new _.fd;this.F=new _.fd;this.G=new _.fd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.gd(_.R)}};var jd;_.id=function(){return _.C(_.hd,_.Vc,5)};jd=class extends _.O{constructor(a){super(a)}};var kd;window.gbar_&&window.gbar_.CONFIG?kd=window.gbar_.CONFIG[0]||{}:kd=[];_.hd=new jd(kd);var bd;bd=_.C(_.hd,$c,3)||new $c;_.Xc=new cd;_.A("gbar_._DumpException",function(a){_.Xc?_.Xc.log(a):console.error(a)});_.ld=new Yc;var nd;_.od=function(a,b){var c=_.md.i();if(a in c.i){if(c.i[a]!=b)throw new nd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.md=class{constructor(){this.i={};this.j={}}static i(){return _.gd(_.md)}};_.pd=class extends _.aa{constructor(){super()}};nd=class extends _.pd{};_.A("gbar.A",_.fd);_.fd.prototype.aa=_.fd.prototype.then;_.A("gbar.B",_.R);_.R.prototype.ba=_.R.prototype.qa;_.R.prototype.bb=_.R.prototype.O;_.R.prototype.bd=_.R.prototype.P;_.R.prototype.bf=_.R.prototype.K;_.R.prototype.bg=_.R.prototype.M;_.R.prototype.bh=_.R.prototype.L;_.R.prototype.bj=_.R.prototype.Y;_.R.prototype.bk=_.R.prototype.J;_.R.prototype.bl=_.R.prototype.N;_.A("gbar.a",_.R.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var qd=new Wc;_.od("api",qd);
var rd=_.id()||new _.Vc,sd=window,td=_.y(_.I(rd,8));sd.__PVT=td;_.od("eq",_.ld);
}catch(e){_._DumpException(e)}
try{
_.ud=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var vd=class extends _.O{constructor(a){super(a)}};var wd=class extends _.P{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.Ma(_.Lc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.G(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var xd=_.C(_.hd,_.Zc,14);if(xd){var yd=_.C(_.hd,_.ud,9)||new _.ud,zd=new vd,Bd=new wd;Bd.init(xd,yd,zd);_.od("gs",Bd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_yeswanth0212@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./AttendanceSystem_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250925-060048_RC00_811285134'; var colabScsVersion = 'b781b5095230a70ef40dcc699a3c1582'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allow_subpaths_in_kernel_url\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_ui_refresh\x22: true, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_bigquery_context\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_custom_context\x22: false, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_generated_cell_placement_logic\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_show_debug_info\x22: false, \x22composer_show_single_diff_buttons\x22: false, \x22composer_survey\x22: true, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22copy_cell_output\x22: true, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22data_inspector\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22disable_output_frame_files\x22: true, \x22disable_text_cell_double_click_presentation_mode\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_markdown_cells\x22: false, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_a100_hm\x22: true, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_composer_changeset_stacking\x22: false, \x22enable_composer_code_report\x22: false, \x22enable_composer_suggestion_chips\x22: true, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: true, \x22enable_improved_composer_context_mentions\x22: false, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22kernel_utils_fetch\x22: false, \x22key_promoter\x22: false, \x22kr\x22: false, \x22light_editor_themes\x22: true, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_ccu_info\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22move_toolbar_icon_to_cell_menu\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: true, \x22multi_modal_context_for_transform\x22: false, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22panel_ui_refresh\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode_connect_runtime\x22: false, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduced_gemini_sparks\x22: true, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222025.07\x22\x5d, \x22runtime_version_selector\x22: true, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: false, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_poll_timeout_ms\x22: 90000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: true, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_cell_editor_toolbar_exit_button\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_ai_service\x22: true, \x22use_colab_adk_service\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730375, 20730485, 20730457, 20730324, 20730476, 20730479, 20730482, 20730150, 20730460, 20730493, 20730177, 20730363, 20730454, 20730182\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_bigquery_context\x22: 45710683, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_custom_context\x22: 45728743, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_generated_cell_placement_logic\x22: 45721730, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_show_debug_info\x22: 45700003, \x22composer_show_single_diff_buttons\x22: 45723066, \x22composer_survey\x22: 45707270, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22converse_notebook_context_length\x22: 45705427, \x22copy_cell_output\x22: 45712093, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22disable_output_frame_files\x22: 45725679, \x22disable_text_cell_double_click_presentation_mode\x22: 45723721, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_markdown_cells\x22: 45707419, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_use_websockets\x22: 45691694, \x22enable_a100_hm\x22: 45723321, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_composer_changeset_stacking\x22: 45717253, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_improved_composer_context_mentions\x22: 45721452, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22kernel_utils_fetch\x22: 45708200, \x22key_promoter\x22: 45425570, \x22light_editor_themes\x22: 45721031, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_ccu_info\x22: 45716751, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22move_toolbar_icon_to_cell_menu\x22: 45726565, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22panel_ui_refresh\x22: 45721124, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode_connect_runtime\x22: 45722751, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduced_gemini_sparks\x22: 45719726, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22runtime_version_selector\x22: 45713197, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22suggest_plots\x22: 45696393, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_cell_editor_toolbar_exit_button\x22: 45723722, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_ai_service\x22: 45713338, \x22use_colab_adk_service\x22: 20730464, \x22user_visible_accelerator_models\x22: 45682571, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'yeswanth0212@gmail.com'; var colabRenderDataToken = 'AFWLbD3Dk9VcVLtBe0fc_IIMgGJEYqNFw03NI4YyooZpG8hAxJ4wl4PpateeNjuseSwtdIrja8n2kz30TQbmDVAewlagxxdDgm2n'; var colabConfig = '\x5b\x5b\x22yeswanth0212@gmail.com\x22,\x5b1,\x22AHXL0D09a+I49\/Wt6t0Z9PqF2TcTc41rtORLGnTcbUx1i\/PE1TwTBc8J9SXjYutmYS6gLm1wGDR+HbzQiveitF2zyzHGpPDoCwErd8VX60XnwNZ\/C0pivcK9ofW3aAzvp0EqnybkUMyqUGnRcNp9dVpS9vIbNoMtxlIlt+tEQA7g5HFUPmXMhgUtWTIdunfvkRrlLEJNd+EuJF20iBf9sqPGm7fv3J511lPvWCM3n4d53gDx6FK8JZudOYuyPOnPV1I3kWXz34ytT6iKpwh2QdD64rUUiSu1b60jUhvknV6uV766V665oYj5sE\/KUhq8WKKLAT+JkBqDpSxtGL4alZvfFgZ6Ou47GgUnnUbG+JxnTR0bG4sNOKBNBb21PkyOFke+ujTR4LZlM3bTlNPbyAJL9BdLSJgl7ES+c2JhIsFCHanrNt9RuHJNwv8Dp1FQagDRQ1i9Vicw4sFRd6A8M5DA0s1ZkwHOaSTQX4dV3Y6Q9\/yIxIolJ9SqMZGhyVBWqzhd1fYtoF6nktRrTqTjR45VNjN2k8WThiLDuKq7xfnd56DTqwqIpfAVC+IR78Xw9YMXhFj6q7DhL7OcRRzS8HnjKKuO8dVxdOwkJlQYjWvWUKYtU+kdR1sFmM0VWjgwEIoge50fL+tyPgd12qus757gKwUEzJ37lgT3qPs7pSBc1iMXOx2q1XmgZJM+GFYs8ngt6Ya6xz6rsKkMNi7ilIEO6ciFNF7BvC3gwMHHdnAz2akZYz1T08wSjOIgCFeoLleY4v8UFfk+5bWFkRwgGjO8LmkKVh0tzN2ALoRyqrf8Nwn0id+S1aDzKpm1aAfbtC30e5S6Xbr6mi\/W8+eYNxdevD\/owpp8dQaKAl6zC8jbR+wo8ylhFGugIKO3ssB0x76DhMqzK3kyks5pBcASeelXfj6DHmEZJm3Z7hqKlbGWZGTlL1XSfBlLY65DtRw5CFYFZU7ZTjHnYp20GCcSn5cESD37w6PzbtqZV7vUnNp6XUxrOcNnN9e2vaOvKq7ouiUMYKHqPd3Gg6TJaLg89Sj48rqPKMgxneFgqvsJpM+niCb++Gbv9\/WXzw7eHgUM++M3cbPucPhqrLsokesQWNMSAn6MzjZoBgoWe3VK3FD4D6FD2D\/GfAtBrC4nmO+cXo6Igkr1HSvMALtgJT1uAF0AQ8SXhqJzXLB1DwLtajqZAYGJixaZaAdUgLtIrBBcXEqDcxXcc5n6HM0r6SwnK7ii3MtZGpK+zV7AB126vy9au3lKvhJLqRerk1UY+6zq7kTpHtlg8HSYk6hSo6\/wFVKmlWkQa+L9n7ceoQ6imsIrAyDBc9GAcyA2F7ubH1+2A9Ca06UVm6FBic8Qx7C+uZBHrp0K8U6z7zYtC7njmsngbClBFqNCj87ZZnGomA6ar2RgfNVWhsC3XjLdxI8is9kzhAvlbTii1Gcma2H6HBtah1yP44j616MQIBf3s0U4XhEYhUZeVPR+nhONMQsmzvro8Z4hoBfzdFqSAkNwqViRr5OgtY1ZDh+KpcN02mOaVs8dR6X0HrnhxaDch4g\/\/+N1QVkIFfSxouAT7ooRTLqrBlxvjYbL1oUHKdusnHLT9f0Ot6Y08QEk52UQUQBIVZCELmR90c15vAZXN+JkBZlGVc4rUJVucrbi1Ry\/Oe2aTeEohFM9zR96BjFowzfeOWGSr+Fc1\/353tJHV7jp4SCbFJkFkSLDkVzpr9VCsCXw6mTTkQVWp++YucIjBV9fjz5XziqUIfJuVsFocOJthd3Y\/el50l5ABavRRtCKYye25FHFN0DELNLucp1p3Hanf\/PmEyb9boeqn+ZeFNiYy2\/yxBI\/kGAslat6hn0XwcRqOBl5BvXaa5RgQJl2i6eSTafy0T50JhTJGwMGqQV4AD0MmHjyscy9FdmCsv88tamkTJ6FmV5qhPNjPSebyRj4jJSWibszrjBB\/cstYDEe4uQ1ICjLgErtZfs9wOOQRUK1yLJHjU2k6nsg\x22,\x22AJ9oCCwUJYjI4jRp8LBCKA+i\/\/mkF6kS0RHpZaHUYv641lwOLJfGU8g0rCFaWey8I4ZANb\/432Eq+yM0hH01tido5RF0Yp8e7YJQ6yU7gRvt9Vhn4kF6gFDfHX0hm85dtFKtuyQ6LvDQ\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/b781b5095230a70ef40dcc699a3c1582/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./AttendanceSystem_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./AttendanceSystem_files/rs=AA2YrTthnASDYd0N4gbIL91FDhrpfXlj5w" nonce=""></script><link type="text/css" href="./AttendanceSystem_files/rs=AA2YrTskOaSug7MVZwlus97OpUaPcMM3bw" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./AttendanceSystem_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./AttendanceSystem_files/editor.main.css"><script async="async" type="text/javascript" src="./AttendanceSystem_files/editor.main.nls.js.download"></script><script src="./AttendanceSystem_files/api.js.download" nonce=""></script><script src="./AttendanceSystem_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #ffffff; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #ffffff;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #ffffff;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: #aceebb;
--vscode-diffEditor-removedTextBackground: #ffcecb;
--vscode-diffEditor-insertedLineBackground: #dafbe1;
--vscode-diffEditor-removedLineBackground: #ffebe9;
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #ffffff;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #ffffff;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #ffffff;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #a53434; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #6a5221; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #9723b4; }
.mtk20 { color: #af00db; }
.mtk21 { color: #a31515; }
.mtk22 { color: #800000; }
.mtk23 { color: #e00000; }
.mtk24 { color: #3030c0; }
.mtk25 { color: #666666; }
.mtk26 { color: #778899; }
.mtk27 { color: #c700c7; }
.mtk28 { color: #4f76ac; }
.mtk29 { color: #008080; }
.mtk30 { color: #001188; }
.mtk31 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script async="async" type="text/javascript" src="./AttendanceSystem_files/python.js.download"></script></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./AttendanceSystem_files/gapi_loader.js.download" nonce=""></script><script src="./AttendanceSystem_files/socketio_binary.js.download" nonce=""></script><script src="./AttendanceSystem_files/analytics_binary.js.download" nonce=""></script><script src="./AttendanceSystem_files/MathJax.js.download" nonce=""></script><script src="./AttendanceSystem_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./AttendanceSystem_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$041847188$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$041847188$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$041847188$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$041847188$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_T" ng-non-bindable=""><div class="gb_Oc"><div>Google Account</div><div class="gb_g">Yeswanth</div><div>yeswanth0212@gmail.com</div><div class="gb_Pc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Gd;Gd=class extends _.pd{};_.Hd=function(a,b){if(b in a.i)return a.i[b];throw new Gd;};_.Id=function(a){return _.Hd(_.md.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Ld;_.Jd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Ld=function(a){return new _.Kd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Md=globalThis.trustedTypes;_.Nd=class{constructor(a){this.i=a}toString(){return this.i}};_.Od=new _.Nd("about:invalid#zClosurez");_.Kd=class{constructor(a){this.Sh=a}};_.Pd=[Ld("data"),Ld("http"),Ld("https"),Ld("mailto"),Ld("ftp"),new _.Kd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Qd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Rd=new _.Qd(_.Md?_.Md.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Vd,fe,ie,Ud,Wd,ae;_.Sd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Td=function(a,b){return a.lastIndexOf(b,0)==0};Vd=function(){let a=null;if(!Ud)return a;try{const b=c=>c;a=Ud.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Xd=function(){Wd===void 0&&(Wd=Vd());return Wd};_.Zd=function(a){const b=_.Xd();a=b?b.createScriptURL(a):a;return new _.Yd(a)};
_.$d=function(a){if(a instanceof _.Yd)return a.i;throw Error("x");};_.be=function(a){if(ae.test(a))return a};_.ce=function(a){if(a instanceof _.Nd)if(a instanceof _.Nd)a=a.i;else throw Error("x");else a=_.be(a);return a};_.de=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.S=function(a,b,c){return _.Ma(_.Lc(a,b,c,_.Kc))};_.ee=function(a,b){return _.Sd(_.Lc(a,b,void 0,_.Kc))};
fe=class extends _.O{constructor(a){super(a)}Xb(a){return _.L(this,24,a)}};_.ge=function(){return _.C(_.hd,fe,1)};_.he=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Ud=_.Md;_.Yd=class{constructor(a){this.i=a}toString(){return this.i+""}};ae=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var oe,se,je;_.le=function(a){return a?new je(_.ke(a)):ie||(ie=new je)};_.me=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.T=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.ne(c,"*",a,b)[0]||null);return a||null};_.ne=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.pe=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:oe.hasOwnProperty(d)?a.setAttribute(oe[d],c):_.Td(d,"aria-")||_.Td(d,"data-")?a.setAttribute(d,c):a[d]=c})};oe={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.qe=function(a){return a?a.defaultView:window};_.te=function(a,b){const c=b[1],d=_.re(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.pe(d,c));b.length>2&&se(a,d,b);return d};se=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.he(f)||_.Lb(f)&&f.nodeType>0?d(f):_.bc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Jd(f):f,d)}};
_.ue=function(a){return _.re(document,a)};_.re=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ve=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.we=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.xe=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ke=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};je=function(a){this.i=a||_.t.document||document};_.n=je.prototype;
_.n.H=function(a){return _.me(this.i,a)};_.n.Qa=function(a,b,c){return _.te(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Je=_.ve;_.n.mg=_.we;_.n.lg=_.xe;
}catch(e){_._DumpException(e)}
try{
_.Mi=function(a){const b=_.de("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Ni=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Zd(a);return b};_.Oi=function(a,b,c){a=a.fa;return _.zb(a,a[_.v]|0,b,c)!==void 0};_.Pi=class extends _.O{constructor(a){super(a)}};_.Qi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Si=function(a,b,c){a<b?Ri(a+1,b):_.Xc.log(Error("W`"+a+"`"+b),{url:c})},Ri=function(a,b){if(Ti){const c=_.ue("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.$d(Ti);_.Mi(c);c.onerror=_.Ob(Si,a,b,c.src);_.Qi("HEAD")[0].appendChild(c)}},Ui=class extends _.O{constructor(a){super(a)}};var Vi=_.C(_.hd,Ui,17)||new Ui,Wi,Ti=(Wi=_.C(Vi,_.Pi,1))?_.Ni(Wi):null,Xi,Yi=(Xi=_.C(Vi,_.Pi,2))?_.Ni(Xi):null,Zi=function(){Ri(1,2);if(Yi){const a=_.ue("LINK");a.setAttribute("type","text/css");a.href=_.$d(Yi).toString();a.rel="stylesheet";let b=_.de("style",document);b&&a.setAttribute("nonce",b);_.Qi("HEAD")[0].appendChild(a)}};(function(){const a=_.ge();if(_.S(a,18))Zi();else{const b=_.ee(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Zi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./AttendanceSystem_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$041847188$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><a id="link" class="button" href="https://colab.research.google.com/drive/1X8EZLdvAMo0N_A9rnAEp8RmI5FRs9A4A#notebook-main"><!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </a>
    </template><!--?lit$041847188$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$041847188$-->
    <!--?lit$041847188$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$041847188$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1X8EZLdvAMo0N_A9rnAEp8RmI5FRs9A4A#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$041847188$--> <!--?lit$041847188$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><div id="header-logo">
              <!--?lit$041847188$--> <!--?lit$041847188$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$041847188$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$041847188$--> <!--?lit$041847188$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 184.538px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">AttendanceSystem.py_</colab-input-sizer>
            <!--?lit$041847188$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$041847188$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$041847188$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$041847188$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$041847188$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$041847188$-->
      <!--?lit$041847188$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$041847188$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$041847188$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$041847188$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->people</md-icon>
                <!--?lit$041847188$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$041847188$--> <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" hidden="" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$041847188$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ha gb_Bd gb_ub gb_bd" id="gb"><div class="gb_0d gb_sb gb_Qd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Ad" style="display:block"><div class="gb_hd"></div><div class="gb_z gb_td gb_Pf gb_1"><div class="gb_D gb_rb gb_Pf gb_1"><a class="gb_B gb_0a gb_1" aria-expanded="false" aria-label="Google Account: Yeswanth  
(yeswanth0212@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><span class="gb_ae"><img class="gb_Q gbii" src="./AttendanceSystem_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyhTJMejSZagsk24LtWZKPo6Wl14K7OwJFphef8G3lG7_g=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyhTJMejSZagsk24LtWZKPo6Wl14K7OwJFphef8G3lG7_g=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_R gb_S" aria-hidden="true"><svg class="gb_La" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ma" cx="7" cy="7" r="7"></circle><path class="gb_Oa" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Cd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Cd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Dd=document.querySelector(".gb_J .gb_B"),Ed=document.querySelector("#gb.gb_7c");Dd&&!Ed&&_.Cd(_.ld,Dd,"click");
}catch(e){_._DumpException(e)}
try{
_.mh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ha()&&a.i[b].B())return a.i[b];return null};_.nh=function(a,b){a.i[b.J()]=b};var oh=new class extends _.P{constructor(){var a=_.Xc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.mh(this)&&_.mh(this).J()==a||this.i[a].P(!0))}Sa(a){this.j=a;for(const b in this.i)this.i[b].ha()&&this.i[b].Sa(a)}lc(a){return a in this.i?this.i[a]:null}};_.od("dd",oh);
}catch(e){_._DumpException(e)}
try{
_.Fi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Gi=document.querySelector(".gb_z .gb_B"),Hi=document.querySelector("#gb.gb_7c");Gi&&!Hi&&_.Cd(_.ld,Gi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$041847188$-->
    <!--?lit$041847188$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$041847188$--><span class="screenreader-only"><!--?lit$041847188$-->Show command palette <!--?lit$041847188$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$041847188$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$041847188$-->Commands
          </colab-toolbar-button>
          <!--?lit$041847188$--><span class="colab-separator"></span><!--?-->
    <!--?lit$041847188$--><span class="toolbar-add-code-split"><colab-toolbar-button class="split-button" command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$041847188$--><span class="screenreader-only"><!--?lit$041847188$-->Insert code cell below <!--?lit$041847188$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$041847188$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$041847188$-->Code
            </colab-toolbar-button>
            <!--?lit$041847188$--></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$041847188$--><span class="screenreader-only"><!--?lit$041847188$-->Add text cell <!--?lit$041847188$--></span>
      </md-text-button>
      <!--?lit$041847188$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$041847188$-->Text
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$041847188$--><span class="screenreader-only"><!--?lit$041847188$-->Run all cells in notebook <!--?lit$041847188$--></span>
      </md-text-button>
      <!--?lit$041847188$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$041847188$-->Run all
      </colab-toolbar-button>
      <!--?lit$041847188$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$041847188$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$041847188$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$041847188$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$041847188$--><!----><md-menu-item command="restart" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item"><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$041847188$-->
    <!--?lit$041847188$-->
    <!--?lit$041847188$-->
    <!--?lit$041847188$-->
    <!--?lit$041847188$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$041847188$-->
    <!--?lit$041847188$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$041847188$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$041847188$--><!--?lit$041847188$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$041847188$--> <!--?lit$041847188$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.34 GB/12.67 GB
Disk: 39.36 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$041847188$--><span class="screenreader-only"><!--?lit$041847188$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.34 GB/12.67 GB
Disk: 39.36 GB/107.72 GB <!--?lit$041847188$--></span>
      </md-text-button>
      <!--?lit$041847188$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.34 GB/12.67 GB
Disk: 39.36 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Connected to</div><!----><!----><div><!--?lit$041847188$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$041847188$-->RAM: 1.34 GB/12.67 GB</div><!----><!----><div><!--?lit$041847188$-->Disk: 39.36 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$041847188$--> <div id="connect-button-resource-display">
          <!--?lit$041847188$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$041847188$-->RAM</div>
      <!--?lit$041847188$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
          <!--?lit$041847188$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$041847188$-->Disk</div>
      <!--?lit$041847188$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        </div>
      </colab-toolbar-button>
      <!--?lit$041847188$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$041847188$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$041847188$-->
    <span class="collapsed-options">
      <!--?lit$041847188$--><span class="colab-separator"></span>
      <!--?lit$041847188$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$041847188$-->
      <!--?lit$041847188$-->
    </span>
    <!--?lit$041847188$--><span class="colab-separator"></span>
    <!--?lit$041847188$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$041847188$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$041847188$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$041847188$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$041847188$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$041847188$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$041847188$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->code</md-icon>
    </md-icon-button> <!--?lit$041847188$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$041847188$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$041847188$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$041847188$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->folder</md-icon>
    </md-icon-button> <!--?lit$041847188$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$041847188$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$041847188$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-LsfR7UByq-12" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$041847188$--><div class="indicator"></div>
      </div>
      <!--?lit$041847188$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$041847188$--><span class="colab-tab-title" id="tab-title-LsfR7UByq-12">
          <!--?lit$041847188$--><!--?lit$041847188$-->Notebook<!--?-->
        </span> <!--?lit$041847188$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$041847188$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$041847188$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$041847188$-->
              <div class="notebook-content ">
                <!--?lit$041847188$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-3gXVS1Z_q-1V" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:01 PM (0 minutes ago)
executed in 11.168s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:01 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 11.168s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[1]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->11s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Install&nbsp;Streamlit&nbsp;and&nbsp;pyngrok</span></span><br><span><span class="mtk6">!</span><span class="mtk1">pip&nbsp;install&nbsp;streamlit&nbsp;pyngrok</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Authenticate&nbsp;ngrok</span></span><br><span><span class="mtk6">!</span><span class="mtk1">ngrok&nbsp;authtoken&nbsp;YOUR_NGROK_AUTH_TOKEN</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-10 output_text"><pre>Collecting streamlit
  Downloading streamlit-1.50.0-py3-none-any.whl.metadata (9.5 kB)
Collecting pyngrok
  Downloading pyngrok-7.4.0-py3-none-any.whl.metadata (8.1 kB)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;7,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;26,&gt;=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)
Collecting pydeck&lt;1,&gt;=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: tornado!=6.5.0,&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: PyYAML&gt;=5.1 in /usr/local/lib/python3.12/dist-packages (from pyngrok) (6.0.2)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (4.25.1)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2.5.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.4.3)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.5.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.8.3)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2025.9.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.27.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
Downloading streamlit-1.50.0-py3-none-any.whl (10.1 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">10.1/10.1 MB</span><span> </span><span style="color: var(--ansi-red);">54.9 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading pyngrok-7.4.0-py3-none-any.whl (25 kB)
Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">6.9/6.9 MB</span><span> </span><span style="color: var(--ansi-red);">85.3 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: pyngrok, pydeck, streamlit
Successfully installed pydeck-0.9.1 pyngrok-7.4.0 streamlit-1.50.0
Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-KZcWqX7dq_rY" tabindex="-1" role="region" aria-label="Cell 1: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution hovered">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:04 PM (0 minutes ago)
executed in 0.045s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:04 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.045s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[3]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->0s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">%%writefile&nbsp;/content/AttendanceSystem.py</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;datetime</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.lib.pagesizes&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;letter</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.pdfgen&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;canvas</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Cadets&nbsp;List</span></span><br><span><span class="mtk1">cadets&nbsp;=&nbsp;[</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;III&nbsp;Year&nbsp;Cadets</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ABISHEK&nbsp;P"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"HARIKARAN&nbsp;G"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ROCHAN&nbsp;M"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHANJAI&nbsp;VADIVEL&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUDHARSAN&nbsp;N"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SURHENDHAAR&nbsp;V"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"VISHNU&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SDA614013"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CQMS"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"YESWANTH&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614015"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DEVADARSHINI&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614016"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JEEVIKA&nbsp;V"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHYANANTHINI&nbsp;D&nbsp;A"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"RAJESHWARI&nbsp;E"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANDHIYA&nbsp;L"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN23SWA614020"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SARIHA&nbsp;SRI&nbsp;K"</span><span class="mtk1">),</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;II&nbsp;Year&nbsp;Cadets</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ADITHYA&nbsp;M"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614002"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ARUNKUMAR&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"BENNY&nbsp;PETER&nbsp;JOHNSON&nbsp;C"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGATHISH&nbsp;S"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614006"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGADEESH&nbsp;V"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JANARTHANAN&nbsp;G"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"KAVIN&nbsp;PRABHAKAR&nbsp;R"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614010"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHISH&nbsp;RAJ&nbsp;A"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANTHOSH&nbsp;KUMAR&nbsp;V"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHARVESH&nbsp;R"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SWA614014"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DHARANI&nbsp;B"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LEGA&nbsp;LAKSHMI&nbsp;A"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MADHUMITHRA&nbsp;N"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MOHANA&nbsp;PRIYA&nbsp;G"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;(</span><span class="mtk21">"TN24SWA614024"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUBASHREE&nbsp;B"</span><span class="mtk1">),</span></span><br><span><span class="mtk1">]</span></span><br><span><span></span></span><br><span><span class="mtk1">st.title(</span><span class="mtk21">"📋&nbsp;NCC&nbsp;Cadets&nbsp;Attendance&nbsp;System"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Initialize&nbsp;attendance</span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk21">"attendance"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance&nbsp;=&nbsp;{cadet:&nbsp;</span><span class="mtk6">False</span><span class="mtk1">&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets}</span></span><br><span><span></span></span><br><span><span class="mtk1">st.subheader(</span><span class="mtk21">"Mark&nbsp;Attendance"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Display&nbsp;checkboxes</span></span><br><span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;reg_no,&nbsp;rank,&nbsp;name&nbsp;=&nbsp;cadet</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;label&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1">{reg_no}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{rank}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{name}</span><span class="mtk21">"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance[cadet]&nbsp;=&nbsp;st.checkb</span><span class="mtk1">ox(label,&nbsp;value=st.session_state.attendance.get(ca</span><span class="mtk1">det,&nbsp;</span><span class="mtk6">False</span><span class="mtk1">))</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Calculate&nbsp;attendance</span></span><br><span><span class="mtk1">present&nbsp;=&nbsp;[c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items()&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;status]</span></span><br><span><span class="mtk1">absent&nbsp;=&nbsp;[c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items()&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;status]</span></span><br><span><span></span></span><br><span><span class="mtk1">total_present&nbsp;=&nbsp;</span><span class="mtk15">len</span><span class="mtk1">(present)</span></span><br><span><span class="mtk1">total_absent&nbsp;=&nbsp;</span><span class="mtk15">len</span><span class="mtk1">(absent)</span></span><br><span><span></span></span><br><span><span class="mtk1">st.write(</span><span class="mtk6">f</span><span class="mtk21">"✅&nbsp;**Total&nbsp;Present:**&nbsp;</span><span class="mtk1">{total_present}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">st.write(</span><span class="mtk6">f</span><span class="mtk21">"❌&nbsp;**Total&nbsp;Absent:**&nbsp;</span><span class="mtk1">{total_absent}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;absent:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write(</span><span class="mtk21">"🚫&nbsp;**Absent&nbsp;Cadets:**"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.write(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;</span><span class="mtk1">{cadet[</span><span class="mtk12">0</span><span class="mtk1">]}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{cadet[</span><span class="mtk12">1</span><span class="mtk1">]}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{cadet[</span><span class="mtk12">2</span><span class="mtk1">]}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.success(</span><span class="mtk21">"🎉&nbsp;All&nbsp;cadets&nbsp;are&nbsp;present&nbsp;today!"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Generate&nbsp;PDF</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">generate_pdf</span><span class="mtk1">(</span><span class="mtk16">filename</span><span class="mtk1">,&nbsp;</span><span class="mtk16">date</span><span class="mtk1">,&nbsp;</span><span class="mtk16">present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">absent</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_absent</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c&nbsp;=&nbsp;canvas.Canvas(filename,&nbsp;pagesize=letter)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;width,&nbsp;height&nbsp;=&nbsp;letter</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont(</span><span class="mtk21">"Helvetica-Bold"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">16</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">200</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Attendance&nbsp;Report"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont(</span><span class="mtk21">"Helvetica"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">12</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">100</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Date:&nbsp;</span><span class="mtk1">{date}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">120</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Present:&nbsp;</span><span class="mtk1">{total_present}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">140</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Absent:&nbsp;</span><span class="mtk1">{total_absent}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">180</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Absent&nbsp;Cadets:"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;=&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">200</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;absent:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;</span><span class="mtk21">"None&nbsp;(All&nbsp;Present)"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1">{cadet[</span><span class="mtk12">0</span><span class="mtk1">]}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{cadet[</span><span class="mtk12">1</span><span class="mtk1">]}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1">{cadet[</span><span class="mtk12">2</span><span class="mtk1">]}</span><span class="mtk21">"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;text)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;-=&nbsp;</span><span class="mtk12">20</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.save()</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button(</span><span class="mtk21">"📥&nbsp;Download&nbsp;Attendance&nbsp;Report&nbsp;as&nbsp;PDF"</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;now&nbsp;=&nbsp;datetime.datetime.now().strftime(</span><span class="mtk21">"%Y-%m-%d&nbsp;%H:%M:%S"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;filename&nbsp;=&nbsp;</span><span class="mtk21">"attendance_report.pdf"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;generate_pdf(filename,&nbsp;now,&nbsp;present,&nbsp;absent,&nbsp;t</span><span class="mtk1">otal_present,&nbsp;total_absent)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;</span><span class="mtk15">open</span><span class="mtk1">(filename,&nbsp;</span><span class="mtk21">"rb"</span><span class="mtk1">)&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;f:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.download_button(</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label=</span><span class="mtk21">"📄&nbsp;Download&nbsp;PDF"</span><span class="mtk1">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data=f,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_name=filename,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mime=</span><span class="mtk21">"application/pdf"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Overwriting /content/AttendanceSystem.py
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-cXMkgGTaroU-" tabindex="-1" role="region" aria-label="Cell 2: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:09 PM (2 minutes ago)
executed in 9.481s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:09 PM (2 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 9.481s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[5]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->9s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">!</span><span class="mtk1">pip&nbsp;install&nbsp;streamlit&nbsp;pyngrok&nbsp;reportlab</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Authenticate&nbsp;ngrok</span></span><br><span><span class="mtk6">!</span><span class="mtk1">ngrok&nbsp;authtoken&nbsp;YOUR_NGROK_AUTH_TOKEN</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Run&nbsp;Streamlit&nbsp;and&nbsp;ngrok</span></span><br><span><span class="mtk6">!</span><span class="mtk1">streamlit&nbsp;run&nbsp;/content/AttendanceSystem.py&nbsp;&amp;&nbsp;npx&nbsp;l</span><span class="mtk1">ocaltunnel&nbsp;--port&nbsp;</span><span class="mtk7">8501</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-14 output_text"><pre>Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.50.0)
Requirement already satisfied: pyngrok in /usr/local/lib/python3.12/dist-packages (7.4.0)
Requirement already satisfied: reportlab in /usr/local/lib/python3.12/dist-packages (4.4.4)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;7,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;26,&gt;=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)
Requirement already satisfied: pydeck&lt;1,&gt;=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: PyYAML&gt;=5.1 in /usr/local/lib/python3.12/dist-packages (from pyngrok) (6.0.2)
Requirement already satisfied: charset-normalizer in /usr/local/lib/python3.12/dist-packages (from reportlab) (3.4.3)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (4.25.1)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2.5.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.5.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.8.3)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2025.9.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.27.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
<span style="color: var(--ansi-red);">ERROR: Operation cancelled by user</span><span style="color: var(--ansi-red);">
</span><span>Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
</span><span>
</span>⠙⠹⠸⠼⠴<span>
</span><span style="font-weight: bold; color: var(--ansi-blue);">  You can now view your Streamlit app in your browser.</span><span>
</span><span>
</span><span style="color: var(--ansi-blue);">  Local URL: </span><span style="font-weight: bold;"><a rel="nofollow" target="_blank" href="http://localhost:8501/">http://localhost:8501</a></span><span>
</span><span style="color: var(--ansi-blue);">  Network URL: </span><span style="font-weight: bold;"><a rel="nofollow" target="_blank" href="http://172.28.0.12:8501/">http://172.28.0.12:8501</a></span><span>
</span><span style="color: var(--ansi-blue);">  External URL: </span><span style="font-weight: bold;"><a rel="nofollow" target="_blank" href="http://34.133.48.218:8501/">http://34.133.48.218:8501</a></span><span>
</span><span>
</span>⠦⠧⠇⠏⠋⠙⠹⠸⠼⠴⠦Need to install the following packages:
localtunnel@2.0.2
Ok to proceed? (y) <span style="color: var(--ansi-blue);">  Stopping...</span><span>
^C
</span></pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-wxPbLnPArpGK" tabindex="-1" role="region" aria-label="Cell 3: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:12 PM (1 minute ago)
executed in 1.335s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:12 PM (1 minute ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 1.335s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[6]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->1s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="19" data-mode-id="notebook-python" style="height: 2005px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/6" style="width: 1367px; height: 2005px;"><div data-mprt="3" class="overflow-guard" style="width: 1367px; height: 2005px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 2005px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 2005px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 2005px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="current-line" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div><div style="position:absolute;top:1311px;width:100%;height:19px;"></div><div style="position:absolute;top:1330px;width:100%;height:19px;"></div><div style="position:absolute;top:1349px;width:100%;height:19px;"></div><div style="position:absolute;top:1368px;width:100%;height:19px;"></div><div style="position:absolute;top:1387px;width:100%;height:19px;"></div><div style="position:absolute;top:1406px;width:100%;height:19px;"></div><div style="position:absolute;top:1425px;width:100%;height:19px;"></div><div style="position:absolute;top:1444px;width:100%;height:19px;"></div><div style="position:absolute;top:1463px;width:100%;height:19px;"></div><div style="position:absolute;top:1482px;width:100%;height:19px;"></div><div style="position:absolute;top:1501px;width:100%;height:19px;"></div><div style="position:absolute;top:1520px;width:100%;height:19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"></div><div style="position:absolute;top:1558px;width:100%;height:19px;"></div><div style="position:absolute;top:1577px;width:100%;height:19px;"></div><div style="position:absolute;top:1596px;width:100%;height:19px;"></div><div style="position:absolute;top:1615px;width:100%;height:19px;"></div><div style="position:absolute;top:1634px;width:100%;height:19px;"></div><div style="position:absolute;top:1653px;width:100%;height:19px;"></div><div style="position:absolute;top:1672px;width:100%;height:19px;"></div><div style="position:absolute;top:1691px;width:100%;height:19px;"></div><div style="position:absolute;top:1710px;width:100%;height:19px;"></div><div style="position:absolute;top:1729px;width:100%;height:19px;"></div><div style="position:absolute;top:1748px;width:100%;height:19px;"></div><div style="position:absolute;top:1767px;width:100%;height:19px;"></div><div style="position:absolute;top:1786px;width:100%;height:19px;"></div><div style="position:absolute;top:1805px;width:100%;height:19px;"></div><div style="position:absolute;top:1824px;width:100%;height:19px;"></div><div style="position:absolute;top:1843px;width:100%;height:19px;"></div><div style="position:absolute;top:1862px;width:100%;height:19px;"></div><div style="position:absolute;top:1881px;width:100%;height:19px;"></div><div style="position:absolute;top:1900px;width:100%;height:19px;"></div><div style="position:absolute;top:1919px;width:100%;height:19px;"></div><div style="position:absolute;top:1938px;width:100%;height:19px;"></div><div style="position:absolute;top:1957px;width:100%;height:19px;"></div><div style="position:absolute;top:1976px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1361px; height: 2005px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 2005px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1361px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:13px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-right-radius" style="top:0px;left:13px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:339px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:339px;width:10px;height:19px;"></div><div class="cslr selected-text top-left-radius top-right-radius" style="top:0px;left:23px;width:316px;height:19px;"></div><svg style="position:absolute;width:301px;height:19px" viewBox="0 0 301 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="296.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr selected-text top-left-radius top-right-radius" style="top:0px;left:0px;width:354px;height:19px;"></div><svg style="position:absolute;width:316px;height:19px" viewBox="0 0 316 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:431px;height:19px;"></div><svg style="position:absolute;width:393px;height:19px" viewBox="0 0 393 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="280.85" cy="9.50" r="1.10"></circle><circle cx="326.85" cy="9.50" r="1.10"></circle><circle cx="388.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:513px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:354px;height:19px;"></div><svg style="position:absolute;width:316px;height:19px" viewBox="0 0 316 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:532px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:354px;height:19px;"></div><svg style="position:absolute;width:316px;height:19px" viewBox="0 0 316 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:551px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:370px;height:19px;"></div><svg style="position:absolute;width:331px;height:19px" viewBox="0 0 331 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="326.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:570px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:400px;height:19px;"></div><svg style="position:absolute;width:362px;height:19px" viewBox="0 0 362 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="280.85" cy="9.50" r="1.10"></circle><circle cx="357.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:589px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:370px;height:19px;"></div><svg style="position:absolute;width:331px;height:19px" viewBox="0 0 331 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="296.85" cy="9.50" r="1.10"></circle><circle cx="326.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:608px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:393px;height:19px;"></div><svg style="position:absolute;width:354px;height:19px" viewBox="0 0 354 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="303.85" cy="9.50" r="1.10"></circle><circle cx="349.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:627px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:346px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:346px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:346px;height:19px;"></div><svg style="position:absolute;width:308px;height:19px" viewBox="0 0 308 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="303.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:646px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:339px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:339px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:339px;height:19px;"></div><svg style="position:absolute;width:301px;height:19px" viewBox="0 0 301 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="296.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:665px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:377px;height:19px;"></div><svg style="position:absolute;width:339px;height:19px" viewBox="0 0 339 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="272.85" cy="9.50" r="1.10"></circle><circle cx="334.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:684px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:370px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:370px;height:19px;"></div><svg style="position:absolute;width:331px;height:19px" viewBox="0 0 331 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="326.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:703px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:377px;height:19px;"></div><svg style="position:absolute;width:339px;height:19px" viewBox="0 0 339 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="288.85" cy="9.50" r="1.10"></circle><circle cx="334.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:346px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:346px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-left-radius bottom-right-radius" style="top:0px;left:0px;width:346px;height:19px;"></div><svg style="position:absolute;width:316px;height:19px" viewBox="0 0 316 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div><div style="position:absolute;top:1311px;width:100%;height:19px;"></div><div style="position:absolute;top:1330px;width:100%;height:19px;"></div><div style="position:absolute;top:1349px;width:100%;height:19px;"></div><div style="position:absolute;top:1368px;width:100%;height:19px;"></div><div style="position:absolute;top:1387px;width:100%;height:19px;"></div><div style="position:absolute;top:1406px;width:100%;height:19px;"></div><div style="position:absolute;top:1425px;width:100%;height:19px;"></div><div style="position:absolute;top:1444px;width:100%;height:19px;"></div><div style="position:absolute;top:1463px;width:100%;height:19px;"></div><div style="position:absolute;top:1482px;width:100%;height:19px;"></div><div style="position:absolute;top:1501px;width:100%;height:19px;"></div><div style="position:absolute;top:1520px;width:100%;height:19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"></div><div style="position:absolute;top:1558px;width:100%;height:19px;"></div><div style="position:absolute;top:1577px;width:100%;height:19px;"></div><div style="position:absolute;top:1596px;width:100%;height:19px;"></div><div style="position:absolute;top:1615px;width:100%;height:19px;"></div><div style="position:absolute;top:1634px;width:100%;height:19px;"></div><div style="position:absolute;top:1653px;width:100%;height:19px;"></div><div style="position:absolute;top:1672px;width:100%;height:19px;"></div><div style="position:absolute;top:1691px;width:100%;height:19px;"></div><div style="position:absolute;top:1710px;width:100%;height:19px;"></div><div style="position:absolute;top:1729px;width:100%;height:19px;"></div><div style="position:absolute;top:1748px;width:100%;height:19px;"></div><div style="position:absolute;top:1767px;width:100%;height:19px;"></div><div style="position:absolute;top:1786px;width:100%;height:19px;"></div><div style="position:absolute;top:1805px;width:100%;height:19px;"></div><div style="position:absolute;top:1824px;width:100%;height:19px;"></div><div style="position:absolute;top:1843px;width:100%;height:19px;"></div><div style="position:absolute;top:1862px;width:100%;height:19px;"></div><div style="position:absolute;top:1881px;width:100%;height:19px;"></div><div style="position:absolute;top:1900px;width:100%;height:19px;"></div><div style="position:absolute;top:1919px;width:100%;height:19px;"></div><div style="position:absolute;top:1938px;width:100%;height:19px;"></div><div style="position:absolute;top:1957px;width:100%;height:19px;"></div><div style="position:absolute;top:1976px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 2005px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1361px; height: 2005px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;datetime</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.lib.pagesizes&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;letter</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.pdfgen&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;canvas</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;=========================</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;III&nbsp;Year&nbsp;Cadets&nbsp;only</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;=========================</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">cadets&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ABISHEK&nbsp;P"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"HARIKARAN&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ROCHAN&nbsp;M"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHANJAI&nbsp;VADIVEL&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUDHARSAN&nbsp;N"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SURHENDHAAR&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"VISHNU&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614013"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CQMS"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"YESWANTH&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614015"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DEVADARSHINI&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614016"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JEEVIKA&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHYANANTHINI&nbsp;D&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"RAJESHWARI&nbsp;E"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANDHIYA&nbsp;L"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614020"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SARIHA&nbsp;SRI&nbsp;K"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;II&nbsp;Year&nbsp;Cadets</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ADITHYA&nbsp;M"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614002"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ARUNKUMAR&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"BENNY&nbsp;PETER&nbsp;JOHNSON&nbsp;C"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGATHISH&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614006"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGADEESH&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JANARTHANAN&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"KAVIN&nbsp;PRABHAKAR&nbsp;R"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614010"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHISH&nbsp;RAJ&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANTHOSH&nbsp;KUMAR&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHARVESH&nbsp;R"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614014"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DHARANI&nbsp;B"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LEGA&nbsp;LAKSHMI&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MADHUMITHRA&nbsp;N"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MOHANA&nbsp;PRIYA&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614024"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUBASHREE&nbsp;B"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📋&nbsp;NCC&nbsp;Cadets&nbsp;Attendance&nbsp;System"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Initialize&nbsp;attendance</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk21">"attendance"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state:</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet:&nbsp;</span><span class="mtk6">False</span><span class="mtk1">&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets</span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">st.subheader</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Mark&nbsp;Attendance"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets:</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;reg_no,&nbsp;rank,&nbsp;name&nbsp;=&nbsp;cadet</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;label&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">reg_no</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">rank</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">name</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">"</span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;st.checkbox</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">label,&nbsp;value=st.session_state.attendance.get</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">cadet,&nbsp;</span><span class="mtk6">False</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Attendance&nbsp;calculation</span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span class="mtk1">present&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;status</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span class="mtk1">absent&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;status</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1083px;height:19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"✅&nbsp;**Total&nbsp;Present:**&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1">present</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1102px;height:19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"❌&nbsp;**Total&nbsp;Absent:**&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1">absent</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1121px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1140px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1159px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🚫&nbsp;**Absent&nbsp;Cadets:**"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1178px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1197px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">2</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1216px;height:19px;" class="view-line"><span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:1235px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.success</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🎉&nbsp;All&nbsp;cadets&nbsp;are&nbsp;present&nbsp;today!"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1254px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1273px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;PDF&nbsp;Report&nbsp;Generation</span></span></div><div style="top:1292px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">generate_pdf</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk16">filename</span><span class="mtk1">,&nbsp;</span><span class="mtk16">date</span><span class="mtk1">,&nbsp;</span><span class="mtk16">present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">absent</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_absent</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:1311px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c&nbsp;=&nbsp;canvas.Canvas</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;pagesize=letter</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1330px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;width,&nbsp;height&nbsp;=&nbsp;letter</span></span></div><div style="top:1349px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1368px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Helvetica-Bold"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">16</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1387px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">200</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Attendance&nbsp;Report"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1406px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1425px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Helvetica"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">12</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1444px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">100</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Date:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">date</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1463px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">120</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Present:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">total_present</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1482px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">140</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Absent:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">total_absent</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1501px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1520px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">180</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Absent&nbsp;Cadets:"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1539px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;=&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">200</span></span></div><div style="top:1558px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1577px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;</span><span class="mtk21">"None&nbsp;(All&nbsp;Present)"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1596px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:1615px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1634px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">2</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">"</span></span></div><div style="top:1653px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;text</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1672px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;-=&nbsp;</span><span class="mtk12">20</span></span></div><div style="top:1691px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1710px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.save</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1729px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1748px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📥&nbsp;Download&nbsp;Attendance&nbsp;Report&nbsp;as&nbsp;PDF"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:1767px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;now&nbsp;=&nbsp;datetime.datetime.now</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.strftime</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"%Y-%m-%d&nbsp;%H:%M:%S"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1786px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;filename&nbsp;=&nbsp;</span><span class="mtk21">"attendance_report.pdf"</span></span></div><div style="top:1805px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;generate_pdf</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;now,&nbsp;present,&nbsp;absent,&nbsp;</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">present</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">absent</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1824px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1843px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;</span><span class="mtk15">open</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;</span><span class="mtk21">"rb"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;f:</span></span></div><div style="top:1862px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.download_button</span><span class="mtk1 bracket-highlighting-0">(</span></span></div><div style="top:1881px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label=</span><span class="mtk21">"📄&nbsp;Download&nbsp;PDF"</span><span class="mtk1">,</span></span></div><div style="top:1900px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data=f,</span></span></div><div style="top:1919px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_name=filename,</span></span></div><div style="top:1938px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mime=</span><span class="mtk21">"application/pdf"</span></span></div><div style="top:1957px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1976px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1361px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 722px; left: 346px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1347px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1347px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="2506" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 2005px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 2005px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 2005px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1367px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 722px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1367px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 2005px;"><div class="minimap-shadow-hidden" style="height: 2005px;"></div><canvas width="0" height="2506" style="position: absolute; left: 0px; width: 0px; height: 2005px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="2506" style="position: absolute; left: 0px; width: 0px; height: 2005px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1528px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 902.22px; max-height: 501.25px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-347 output_text"><pre>2025-09-29 13:40:41.699 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.783 
  <span style="font-weight: bold; color: var(--ansi-yellow);">Warning:</span><span> to view this Streamlit app on a browser, run it with the following
  command:

    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]
2025-09-29 13:40:41.784 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.784 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.786 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.787 Session state does not function when running a script without `streamlit run`
2025-09-29 13:40:41.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.790 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.792 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.793 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.793 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.795 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.796 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.797 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.798 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.799 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.801 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.804 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.804 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.805 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.808 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.809 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.813 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.814 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.823 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.825 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.828 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.829 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.829 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.831 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.831 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.832 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.833 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.834 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.835 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.835 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.836 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.837 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.837 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.838 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.838 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.839 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.840 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.840 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.841 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.842 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.842 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.843 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.843 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.844 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.845 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.847 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.848 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.848 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.849 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.850 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.852 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.853 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.853 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.854 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.854 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.855 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.856 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.856 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.858 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.861 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.861 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.862 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.862 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.863 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.865 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.865 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.866 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.866 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.867 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.869 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.869 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.870 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.870 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.872 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.872 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.873 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.873 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.874 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.874 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.875 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.875 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.876 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.876 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.877 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.878 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.878 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.879 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.879 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.880 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.880 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.881 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.882 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.882 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.882 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.884 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.885 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.885 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.886 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.886 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.887 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.887 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.889 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.889 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.890 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.890 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.893 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.893 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.894 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.896 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.896 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.897 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.897 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.898 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.898 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.898 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.902 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.902 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.903 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.903 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.905 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.908 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.909 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.910 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.910 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.911 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.912 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.912 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.913 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.913 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.916 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.916 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.917 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.917 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.918 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.920 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.920 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.921 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.921 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.922 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.922 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.924 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.924 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.924 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.925 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.925 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.926 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.927 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.927 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.928 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.928 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.929 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.930 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.930 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.931 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.932 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.932 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.933 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.933 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.934 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.935 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.935 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.936 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.936 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.937 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.937 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.938 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.940 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.941 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.941 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.943 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.943 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.944 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.945 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.945 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.946 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.946 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.947 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.947 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.949 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.950 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.950 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.951 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.951 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.952 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.952 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.953 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.953 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.954 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.954 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.956 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.956 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.957 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.959 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.959 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.960 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.960 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.961 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.962 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.962 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.963 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.963 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.964 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.967 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.967 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.968 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.968 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.969 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.969 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.970 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.970 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.971 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.971 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.972 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.972 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.973 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.973 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.975 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.977 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.978 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.978 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.979 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.979 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.979 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.980 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.980 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.982 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.985 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.985 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.987 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.987 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.988 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.990 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.990 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.991 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.991 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.992 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.992 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.993 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.993 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.994 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.995 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.996 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.998 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:41.998 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.000 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.002 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.004 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.005 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.006 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.008 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.008 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.009 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.009 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-09-29 13:40:42.010 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
</span></pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-aNyrNOlet6Fk" tabindex="-1" role="region" aria-label="Cell 4: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:14 PM (0 minutes ago)
executed in 4.71s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:14 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 4.71s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[7]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->4s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">!</span><span class="mtk1">pip&nbsp;install&nbsp;streamlit&nbsp;pyngrok&nbsp;reportlab</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.50.0)
Requirement already satisfied: pyngrok in /usr/local/lib/python3.12/dist-packages (7.4.0)
Requirement already satisfied: reportlab in /usr/local/lib/python3.12/dist-packages (4.4.4)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;7,&gt;=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;26,&gt;=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)
Requirement already satisfied: pydeck&lt;1,&gt;=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: PyYAML&gt;=5.1 in /usr/local/lib/python3.12/dist-packages (from pyngrok) (6.0.2)
Requirement already satisfied: charset-normalizer in /usr/local/lib/python3.12/dist-packages (from reportlab) (3.4.3)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (4.25.1)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2.5.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.5.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.8.3)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2025.9.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.27.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-JEEXJAlIt6yI" tabindex="-1" role="region" aria-label="Cell 5: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:14 PM (0 minutes ago)
executed in 0.175s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:14 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.175s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[8]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->0s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre tabindex="0" class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">!</span><span class="mtk1">ngrok&nbsp;authtoken&nbsp;</span><span class="mtk21">"33NEYBEvzXfsNRgckQgH7vLXdRX_2jvarbZ7sSCnweeLXJyH7</span><span class="mtk21">"</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh code-has-output" id="cell-UFqMJDIFuBue" tabindex="-1" role="region" aria-label="Cell 6: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:21 PM (0 minutes ago)
executed in 0.026s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:21 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.026s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[11]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->0s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="33" data-mode-id="notebook-python" style="height: 2043px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/9" style="width: 1367px; height: 2043px;"><div data-mprt="3" class="overflow-guard" style="width: 1367px; height: 2043px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 2043px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 2043px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 2043px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div><div style="position:absolute;top:1311px;width:100%;height:19px;"></div><div style="position:absolute;top:1330px;width:100%;height:19px;"></div><div style="position:absolute;top:1349px;width:100%;height:19px;"></div><div style="position:absolute;top:1368px;width:100%;height:19px;"></div><div style="position:absolute;top:1387px;width:100%;height:19px;"></div><div style="position:absolute;top:1406px;width:100%;height:19px;"></div><div style="position:absolute;top:1425px;width:100%;height:19px;"></div><div style="position:absolute;top:1444px;width:100%;height:19px;"></div><div style="position:absolute;top:1463px;width:100%;height:19px;"></div><div style="position:absolute;top:1482px;width:100%;height:19px;"></div><div style="position:absolute;top:1501px;width:100%;height:19px;"></div><div style="position:absolute;top:1520px;width:100%;height:19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"></div><div style="position:absolute;top:1558px;width:100%;height:19px;"></div><div style="position:absolute;top:1577px;width:100%;height:19px;"></div><div style="position:absolute;top:1596px;width:100%;height:19px;"></div><div style="position:absolute;top:1615px;width:100%;height:19px;"></div><div style="position:absolute;top:1634px;width:100%;height:19px;"></div><div style="position:absolute;top:1653px;width:100%;height:19px;"></div><div style="position:absolute;top:1672px;width:100%;height:19px;"></div><div style="position:absolute;top:1691px;width:100%;height:19px;"></div><div style="position:absolute;top:1710px;width:100%;height:19px;"></div><div style="position:absolute;top:1729px;width:100%;height:19px;"></div><div style="position:absolute;top:1748px;width:100%;height:19px;"></div><div style="position:absolute;top:1767px;width:100%;height:19px;"></div><div style="position:absolute;top:1786px;width:100%;height:19px;"></div><div style="position:absolute;top:1805px;width:100%;height:19px;"></div><div style="position:absolute;top:1824px;width:100%;height:19px;"></div><div style="position:absolute;top:1843px;width:100%;height:19px;"></div><div style="position:absolute;top:1862px;width:100%;height:19px;"></div><div style="position:absolute;top:1881px;width:100%;height:19px;"></div><div style="position:absolute;top:1900px;width:100%;height:19px;"></div><div style="position:absolute;top:1919px;width:100%;height:19px;"></div><div style="position:absolute;top:1938px;width:100%;height:19px;"></div><div style="position:absolute;top:1957px;width:100%;height:19px;"></div><div style="position:absolute;top:1976px;width:100%;height:19px;"></div><div style="position:absolute;top:1995px;width:100%;height:19px;"></div><div style="position:absolute;top:2014px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1361px; height: 2043px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 2043px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1361px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1361px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"></div><div style="position:absolute;top:1254px;width:100%;height:19px;"></div><div style="position:absolute;top:1273px;width:100%;height:19px;"></div><div style="position:absolute;top:1292px;width:100%;height:19px;"></div><div style="position:absolute;top:1311px;width:100%;height:19px;"></div><div style="position:absolute;top:1330px;width:100%;height:19px;"></div><div style="position:absolute;top:1349px;width:100%;height:19px;"></div><div style="position:absolute;top:1368px;width:100%;height:19px;"></div><div style="position:absolute;top:1387px;width:100%;height:19px;"></div><div style="position:absolute;top:1406px;width:100%;height:19px;"></div><div style="position:absolute;top:1425px;width:100%;height:19px;"></div><div style="position:absolute;top:1444px;width:100%;height:19px;"></div><div style="position:absolute;top:1463px;width:100%;height:19px;"></div><div style="position:absolute;top:1482px;width:100%;height:19px;"></div><div style="position:absolute;top:1501px;width:100%;height:19px;"></div><div style="position:absolute;top:1520px;width:100%;height:19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"></div><div style="position:absolute;top:1558px;width:100%;height:19px;"></div><div style="position:absolute;top:1577px;width:100%;height:19px;"></div><div style="position:absolute;top:1596px;width:100%;height:19px;"></div><div style="position:absolute;top:1615px;width:100%;height:19px;"></div><div style="position:absolute;top:1634px;width:100%;height:19px;"></div><div style="position:absolute;top:1653px;width:100%;height:19px;"></div><div style="position:absolute;top:1672px;width:100%;height:19px;"></div><div style="position:absolute;top:1691px;width:100%;height:19px;"></div><div style="position:absolute;top:1710px;width:100%;height:19px;"></div><div style="position:absolute;top:1729px;width:100%;height:19px;"></div><div style="position:absolute;top:1748px;width:100%;height:19px;"></div><div style="position:absolute;top:1767px;width:100%;height:19px;"></div><div style="position:absolute;top:1786px;width:100%;height:19px;"></div><div style="position:absolute;top:1805px;width:100%;height:19px;"></div><div style="position:absolute;top:1824px;width:100%;height:19px;"></div><div style="position:absolute;top:1843px;width:100%;height:19px;"></div><div style="position:absolute;top:1862px;width:100%;height:19px;"></div><div style="position:absolute;top:1881px;width:100%;height:19px;"></div><div style="position:absolute;top:1900px;width:100%;height:19px;"></div><div style="position:absolute;top:1919px;width:100%;height:19px;"></div><div style="position:absolute;top:1938px;width:100%;height:19px;"></div><div style="position:absolute;top:1957px;width:100%;height:19px;"></div><div style="position:absolute;top:1976px;width:100%;height:19px;"></div><div style="position:absolute;top:1995px;width:100%;height:19px;"></div><div style="position:absolute;top:2014px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 2043px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1361px; height: 2043px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">%%writefile&nbsp;</span><span class="mtk6 detected-link">/content/AttendanceSystem.py</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;datetime</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.lib.pagesizes&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;letter</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;reportlab.pdfgen&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;canvas</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;datetime</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;pytz</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;=========================</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;III&nbsp;Year&nbsp;Cadets&nbsp;only</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;=========================</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">cadets&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ABISHEK&nbsp;P"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"HARIKARAN&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ROCHAN&nbsp;M"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHANJAI&nbsp;VADIVEL&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUDHARSAN&nbsp;N"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SURHENDHAAR&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"VISHNU&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SDA614013"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CQMS"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"YESWANTH&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614015"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SGT"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DEVADARSHINI&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614016"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CUO"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JEEVIKA&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHYANANTHINI&nbsp;D&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"RAJESHWARI&nbsp;E"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANDHIYA&nbsp;L"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN23SWA614020"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"CSM"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SARIHA&nbsp;SRI&nbsp;K"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614001"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ADITHYA&nbsp;M"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614002"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"ARUNKUMAR&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614003"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"BENNY&nbsp;PETER&nbsp;JOHNSON&nbsp;C"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614005"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGATHISH&nbsp;S"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614006"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JAGADEESH&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614007"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"JANARTHANAN&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614009"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"KAVIN&nbsp;PRABHAKAR&nbsp;R"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614010"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"NITHISH&nbsp;RAJ&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614011"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SANTHOSH&nbsp;KUMAR&nbsp;V"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SDA614012"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SHARVESH&nbsp;R"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614014"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"DHARANI&nbsp;B"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614017"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LEGA&nbsp;LAKSHMI&nbsp;A"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614018"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MADHUMITHRA&nbsp;N"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614019"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"MOHANA&nbsp;PRIYA&nbsp;G"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk21">"TN24SWA614024"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"LCPL"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"SUBASHREE&nbsp;B"</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📋&nbsp;NCC&nbsp;Cadets&nbsp;Attendance&nbsp;System"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Initialize&nbsp;attendance</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk21">"attendance"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state:</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet:&nbsp;</span><span class="mtk6">False</span><span class="mtk1">&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets</span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk1">st.subheader</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Mark&nbsp;Attendance"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;cadets:</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;reg_no,&nbsp;rank,&nbsp;name&nbsp;=&nbsp;cadet</span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;label&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">reg_no</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">rank</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">name</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">"</span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.attendance</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;st.checkbox</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">label,&nbsp;value=st.session_state.attendance.get</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">cadet,&nbsp;</span><span class="mtk6">False</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Attendance&nbsp;calculation</span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span class="mtk1">present&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;status</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span class="mtk1">absent&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;c,&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;st.session_state.attendance.items</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;status</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:1083px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1102px;height:19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"✅&nbsp;**Total&nbsp;Present:**&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1">present</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1121px;height:19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"❌&nbsp;**Total&nbsp;Absent:**&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1">absent</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1140px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1159px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1178px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🚫&nbsp;**Absent&nbsp;Cadets:**"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1197px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1216px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk12">2</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1235px;height:19px;" class="view-line"><span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:1254px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.success</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🎉&nbsp;All&nbsp;cadets&nbsp;are&nbsp;present&nbsp;today!"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1273px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1292px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;PDF&nbsp;Report&nbsp;Generation</span></span></div><div style="top:1311px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">generate_pdf</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk16">filename</span><span class="mtk1">,&nbsp;</span><span class="mtk16">date</span><span class="mtk1">,&nbsp;</span><span class="mtk16">present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">absent</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_present</span><span class="mtk1">,&nbsp;</span><span class="mtk16">total_absent</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:1330px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c&nbsp;=&nbsp;canvas.Canvas</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;pagesize=letter</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1349px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;width,&nbsp;height&nbsp;=&nbsp;letter</span></span></div><div style="top:1368px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1387px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Helvetica-Bold"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">16</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1406px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">200</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Attendance&nbsp;Report"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1425px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1444px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.setFont</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Helvetica"</span><span class="mtk1">,&nbsp;</span><span class="mtk12">12</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1463px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">100</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Date:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">date</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1482px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">120</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Present:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">total_present</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1501px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">140</span><span class="mtk1">,&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Total&nbsp;Absent:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">total_absent</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1520px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1539px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">50</span><span class="mtk1">,&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">180</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"Absent&nbsp;Cadets:"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1558px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;=&nbsp;height&nbsp;-&nbsp;</span><span class="mtk12">200</span></span></div><div style="top:1577px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1596px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;</span><span class="mtk21">"None&nbsp;(All&nbsp;Present)"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1615px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:1634px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;cadet&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;absent:</span></span></div><div style="top:1653px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">&nbsp;</span><span class="mtk1">|</span><span class="mtk21">&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span><span class="mtk1">cadet</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">2</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">}</span><span class="mtk21">"</span></span></div><div style="top:1672px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.drawString</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;y,&nbsp;text</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1691px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;-=&nbsp;</span><span class="mtk12">20</span></span></div><div style="top:1710px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1729px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;c.save</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1748px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1767px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📥&nbsp;Download&nbsp;Attendance&nbsp;Report&nbsp;as&nbsp;PDF"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:1786px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;india_tz&nbsp;=&nbsp;pytz.timezone</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Asia/Kolkata"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1805px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;now&nbsp;=&nbsp;datetime.datetime.now</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">india_tz</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">.strftime</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"%Y-%m-%d&nbsp;%H:%M:%S"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1824px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;filename&nbsp;=&nbsp;</span><span class="mtk21">"attendance_report.pdf"</span></span></div><div style="top:1843px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;generate_pdf</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;now,&nbsp;present,&nbsp;absent,&nbsp;</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">present</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;</span><span class="mtk15">len</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">absent</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:1862px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1881px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;</span><span class="mtk15">open</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">filename,&nbsp;</span><span class="mtk21">"rb"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;f:</span></span></div><div style="top:1900px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.download_button</span><span class="mtk1 bracket-highlighting-0">(</span></span></div><div style="top:1919px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label=</span><span class="mtk21">"📄&nbsp;Download&nbsp;PDF"</span><span class="mtk1">,</span></span></div><div style="top:1938px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data=f,</span></span></div><div style="top:1957px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_name=filename,</span></span></div><div style="top:1976px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mime=</span><span class="mtk21">"application/pdf"</span></span></div><div style="top:1995px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:2014px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1347px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1347px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="2553" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 2043px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 2043px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 2043px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1367px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1367px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 2043px;"><div class="minimap-shadow-hidden" style="height: 2043px;"></div><canvas width="0" height="2553" style="position: absolute; left: 0px; width: 0px; height: 2043px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="2553" style="position: absolute; left: 0px; width: 0px; height: 2043px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1528px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 902.22px; max-height: 510.75px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 6 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Overwriting /content/AttendanceSystem.py
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh focused code-has-output" id="cell-xjmQv7dJuOif" tabindex="-1" role="region" aria-label="Cell 7: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->arrow_upward</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Move cell up</div><!----><!----><div><!--?lit$041847188$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->arrow_downward</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Move cell down</div><!----><!----><div><!--?lit$041847188$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$041847188$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-xjmQv7dJuOif" anchor="ai-menu-anchor-xjmQv7dJuOif" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$041847188$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$041847188$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$041847188$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$041847188$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-xjmQv7dJuOif-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-xjmQv7dJuOif" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>
              <!--?lit$041847188$-->pen_spark
            </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-xjmQv7dJuOif" id="ai-menu-anchor-xjmQv7dJuOif-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->link</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->comment</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Add a comment</div><!----><!----><div><!--?lit$041847188$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->settings</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->edit</md-icon>
        <!--?lit$041847188$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->delete</md-icon>
        <!--?lit$041847188$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Delete cell</div><!----><!----><div><!--?lit$041847188$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$041847188$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:24 PM (0 minutes ago)
executed in 0.205s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:24 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.205s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[14]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->0s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="22" data-mode-id="notebook-python" style="height: 257px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/10" style="width: 1367px; height: 257px;"><div data-mprt="3" class="overflow-guard" style="width: 1367px; height: 257px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 257px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 257px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 257px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="current-line" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1361px; height: 257px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 257px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1361px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cslr selected-text top-left-radius bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:92px;height:19px;"></div><svg style="position:absolute;width:8px;height:19px" viewBox="0 0 8 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"></svg></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1361px; height: 257px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;pyngrok&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;ngrok</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;subprocess</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Kill&nbsp;old&nbsp;tunnels&nbsp;if&nbsp;running</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">ngrok.kill</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Start&nbsp;new&nbsp;tunnel</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">public_url&nbsp;=&nbsp;ngrok.connect</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk12">8501</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🚀&nbsp;Public&nbsp;URL:"</span><span class="mtk1">,&nbsp;public_url</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Launch&nbsp;Streamlit&nbsp;app</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">subprocess.Popen</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk21">"streamlit"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"run"</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"</span><span class="mtk21 detected-link">/content/AttendanceSystem.py</span><span class="mtk21">"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon-light-bulb codicon" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1361px; top: 57px; left: 0px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 76px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1347px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1347px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="321" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 257px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 257px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 257px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1367px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 76px; left: 6px; width: 76992px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1367px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 257px;"><div class="minimap-shadow-hidden" style="height: 257px;"></div><canvas width="0" height="321" style="position: absolute; left: 0px; width: 0px; height: 257px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="321" style="position: absolute; left: 0px; width: 0px; height: 257px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1528px; top: 383.15px; left: 286.4px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 8px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 0px; height: 0px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 902.22px; max-height: 250px; width: 0px; height: 0px;"><div class="hover-row markdown-hover"><div class="hover-contents"><div class="rendered-markdown"><p>Loading...</p></div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal fade" style="position: absolute; width: 0px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 0px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 0px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 7 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>🚀 Public URL: NgrokTunnel: "<a rel="nofollow" target="_blank" href="https://2c6f01a15646.ngrok-free.app/">https://2c6f01a15646.ngrok-free.app</a>" -&gt; "<a rel="nofollow" target="_blank" href="http://localhost:8501/">http://localhost:8501</a>"
</pre></div><div class="execute_result output-id-2 output_text"><pre>&lt;Popen: returncode: None args: ['streamlit', 'run', '/content/AttendanceSyst...&gt;</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh" id="cell-xps-qIJIuPIZ" tabindex="-1" role="region" aria-label="Cell 8: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Yeswanth
7:24 PM (0 minutes ago)
executed in 0.004s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->executed by Yeswanth</div><!----><!----><div><!--?lit$041847188$-->7:24 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.004s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[13]</div>
      <!--?lit$041847188$--><div class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->check</md-icon>
      <div><!--?lit$041847188$-->0s</div>
    </div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="34" data-mode-id="notebook-python" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/11" style="width: 1367px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 1367px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1361px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1361px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1361px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1361px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">ngrok.kill</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1347px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1347px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="36" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1367px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1367px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1528px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 902.22px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 8 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$--><svg viewBox="0 0 24 24"><!--?lit$041847188$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell cell-ui-refresh" id="cell-VXrczmEbwN4c" tabindex="-1" role="region" aria-label="Cell 9: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$041847188$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$041847188$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$041847188$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$041847188$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$041847188$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$041847188$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$041847188$--><div class="status">
      <div class="execution-count"><!--?lit$041847188$-->[ ]</div>
      <!--?lit$041847188$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="32" data-mode-id="notebook-python" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/12" style="width: 1367px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 1367px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1361px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1361px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1361px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1361px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><colab-cell-placeholder widgetid="editor.widget.cellPlaceholderHint" style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; position: absolute; display: block; visibility: inherit; max-width: 1361px; top: 0px; left: 0px;" monaco-visible-content-widget="true"><template shadowrootmode="open"><!----><div><!--?lit$041847188$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-cell-placeholder></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1347px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1347px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="36" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1367px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1367px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1528px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 902.22px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 9 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$041847188$-->Text
        </md-outlined-button>
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$041847188$--> <div class="footer-links" style="padding-bottom: 155.594px;">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$041847188$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$041847188$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$041847188$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$041847188$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$041847188$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$041847188$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$041847188$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$041847188$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$041847188$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$041847188$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$041847188$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$041847188$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./AttendanceSystem_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./AttendanceSystem_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowrootmode="open"><!---->
      <md-icon-button toggle="" id="toggle-composer-button" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <!--?lit$041847188$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer-button" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-composer view-mode="floating" class="" style="transform: translate(0px, 0px);"><template shadowrootmode="open"><!---->
      <colab-composer-conversation><template shadowrootmode="open"><!---->
      <div class="scrollable">
        <!--?lit$041847188$-->
        <!--?lit$041847188$-->
      </div>
    </template>
      </colab-composer-conversation>
      <!--?lit$041847188$-->
      <div class="footer">
        <!--?lit$041847188$--> <!--?lit$041847188$-->
      <div class="suggestion-chips">
        <!--?lit$041847188$--><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$-->How can I install Python libraries?
      </md-outlined-button>
    <!----><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$-->Load data from Google Drive
      </md-outlined-button>
    <!----><!---->
      <md-outlined-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <!--?lit$041847188$-->Show an example of training a simple ML model
      </md-outlined-button>
    <!---->
      </div>
    
        <div class="input-container">
          <colab-composer-input><template shadowrootmode="open"><!---->
      <div class="wrapper">
        <!--?lit$041847188$--><colab-composer-attachments removable=""><template shadowrootmode="open"><!---->
      <md-chip-set class="attachments"><template shadowrootmode="open"><!----><slot></slot></template>
        <!--?lit$041847188$--><!---->
        <md-input-chip has-icon="" class="  " tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <div class="container  has-icon has-trailing ">
        <!--?lit$041847188$-->
      <!--?lit$041847188$-->
      <!--?lit$041847188$--><span class="outline"></span>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$-->
      <button class="primary action" id="button" type="button"><!--?lit$041847188$-->
      <span class="leading icon" aria-hidden="true">
        <!--?lit$041847188$--><slot name="icon"></slot>
      </span>
      <span class="label">
        <span class="label-text" id="label">
          <!--?lit$041847188$--><slot></slot>
        </span>
      </span>
      <span class="touch"></span>
    </button>
    
    
      <!--?lit$041847188$-->
    <span id="remove-label" hidden="" aria-hidden="true">Remove</span>
    <button class="trailing action" aria-labelledby="remove-label label" tabindex="-1">
      <md-focus-ring part="trailing-focus-ring" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <span class="trailing icon" aria-hidden="true">
        <slot name="remove-trailing-icon">
          <svg viewBox="0 96 960 960">
            <path d="m249 849-42-42 231-231-231-231 42-42 231 231 231-231 42 42-231 231 231 231-42 42-231-231-231 231Z"></path>
          </svg>
        </slot>
      </span>
      <span class="touch"></span>
    </button>
  
    
      </div>
    </template>
          <!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>
          <!--?lit$041847188$-->code
        </md-icon> <!--?lit$041847188$--><!--?lit$041847188$-->Empty cell<!--?-->
        </md-input-chip>
      <!---->
      </md-chip-set>
    </template>
    </colab-composer-attachments>
        <!--?lit$041847188$-->
              <div class="text-field-and-spark">
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$041847188$-->
          <div class="text-field-wrapper" data-value="">
            <md-outlined-text-field type="textarea" aria-controls="autocomplete-menu" rows="1" data-aria-autocomplete="list" class="composer-input-field" data-aria-expanded="false" maxlength="2000" placeholder="What can I help you build?" inputmode="" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field  textarea ">
        <!--?lit$041847188$--><md-outlined-field class="field" count="0" error-text="" label="" max="2000" resizable="" supporting-text=""><template shadowrootmode="open"><!---->
      <div class="field resizable no-label">
        <div class="container-overflow">
          <!--?lit$041847188$-->
          <slot name="container"></slot>
          <!--?lit$041847188$--> <!--?lit$041847188$--> <!--?lit$041847188$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$041847188$--></div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$041847188$--> <!--?lit$041847188$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$041847188$-->
      <div class="supporting-text"><!--?lit$041847188$--><span><!--?lit$041847188$--></span><!--?lit$041847188$--><span class="counter"><!--?lit$041847188$-->0 / 2000</span></div>
      <slot name="aria-describedby"></slot>
    
      </div>
    </template>
      <!--?lit$041847188$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$041847188$-->
        <textarea class="input" aria-describedby="description" aria-invalid="false" maxlength="2000" placeholder="What can I help you build?" rows="1" cols="20"></textarea>
      
      <!--?lit$041847188$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby" hidden=""><!----><!--?lit$041847188$--> <!--?lit$041847188$-->0 / 2000<!--?--></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
            </md-outlined-text-field>
            <!--?lit$041847188$-->
          </div>
        
              </div>
              <div class="actions">
                <!--?lit$041847188$--><md-icon-button data-aria-haspopup="true" id="add-context" data-aria-label="Add to Gemini" data-aria-expanded="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add to Gemini" aria-haspopup="true" aria-expanded="false">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add_circle</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="add-context" message="Add to Gemini"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Add to Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-menu positioning="popover" quick="" aria-labelledby="add-context" anchor="add-context" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$041847188$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$041847188$--><slot></slot> </div>
        </div>
      </div>
    </template>
        <!--?lit$041847188$-->
      <md-menu-item md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>folder</md-icon>
        <span slot="headline"><!--?lit$041847188$-->Select files</span>
      </md-menu-item>
      <md-menu-item md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$041847188$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$041847188$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$041847188$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$041847188$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload</md-icon>
        <span slot="headline"><!--?lit$041847188$-->Upload</span>
      </md-menu-item>
    
        <!--?lit$041847188$-->
      </md-menu>
                <!--?lit$041847188$--><md-icon-button id="send" data-aria-label="Send" aria-describedby="send-tooltip" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Send" aria-disabled="true">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>send</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="send" id="send-tooltip" message="Send"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Send</div><!----><!--?--></template>
      </colab-tooltip-trigger>
              </div>
            
      </div>
      <!--?lit$041847188$-->
      <input type="file" hidden="" multiple="">
    </template></colab-composer-input>
          <!--?lit$041847188$--><div class="floating-actions">
      <!--?lit$041847188$--><!--?lit$041847188$-->
      <md-icon-button id="move-to-side-panel" data-aria-label="Move to panel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move to panel">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dock_to_left</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="move-to-side-panel" message="Move to panel"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Move to panel</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    <!--?lit$041847188$--><md-icon-button id="close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$041847188$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$041847188$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$041847188$--><span class="icon"><slot></slot></span>
        <!--?lit$041847188$-->
        <!--?lit$041847188$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="close" message="Close"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Close</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?-->
    </div>
        </div>
        <!--?lit$041847188$--> <!--?lit$041847188$-->
      </div>
      <!--?lit$041847188$-->
    
    </template></colab-composer><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="middle"><!--?lit$041847188$--></span>
      <span class="right">
        <!--?lit$041847188$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template><!--?lit$041847188$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon><!--?lit$041847188$-->7:24 PM</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Focus the last run cell

7:24 PM (0 minutes ago)
executed in 0.191s"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Focus the last run cell</div><!----><!----><br><!----><!----><div><!--?lit$041847188$-->7:24 PM (0 minutes ago)</div><!----><!----><div><!--?lit$041847188$-->executed in 0.191s</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$041847188$--><!--?lit$041847188$--><!--?lit$041847188$--><colab-runtime-status><template shadowrootmode="open"><!----><md-text-button data-aria-expanded="false" data-aria-haspopup="menu" id="runtime-options" aria-describedby="runtime-options-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button" aria-haspopup="menu" aria-expanded="false">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dns</md-icon><!--?lit$041847188$-->Python 3</md-text-button><colab-tooltip-trigger aria-hidden="true" for="runtime-options" id="runtime-options-tooltip" message="Runtime options"><template shadowrootmode="open"><!----><!--?lit$041847188$--><!----><div><!--?lit$041847188$-->Runtime options</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->data_object</md-icon>
        <!--?lit$041847188$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$041847188$-->terminal</md-icon>
        <!--?lit$041847188$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 719px; visibility: visible; left: 68px; top: 62px; display: none;"><!--?lit$041847188$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Locate in Drive<!--?lit$041847188$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Open in playground mode<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->New notebook in Drive<!--?lit$041847188$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Open notebook<!--?lit$041847188$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Upload notebook<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Rename<!--?lit$041847188$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Move<!--?lit$041847188$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Move to trash<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save a copy in Drive<!--?lit$041847188$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save a copy as a GitHub Gist<!--?lit$041847188$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save a copy in GitHub<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save<!--?lit$041847188$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save and pin revision<!--?lit$041847188$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Revision history<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$041847188$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Print<!--?lit$041847188$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Download .ipynb<!--?lit$041847188$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Download .py<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Undo<!--?lit$041847188$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Redo<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Select all cells<!--?lit$041847188$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Cut cell or selection<!--?lit$041847188$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Copy cell or selection<!--?lit$041847188$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Paste<!--?lit$041847188$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Delete selected cells<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Find and replace<!--?lit$041847188$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Find next<!--?lit$041847188$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Find previous<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Notebook settings<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Clear all outputs<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$041847188$-->Table of contents<!--?lit$041847188$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Notebook info<!--?lit$041847188$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Executed code history<!--?lit$041847188$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Start slideshow<!--?lit$041847188$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Start slideshow from beginning<!--?lit$041847188$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$041847188$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Collapse sections<!--?lit$041847188$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Expand sections<!--?lit$041847188$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Save collapsed section layout<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Show/hide code<!--?lit$041847188$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Show/hide output<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Focus next tab<!--?lit$041847188$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Focus previous tab<!--?lit$041847188$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Move tab to next pane<!--?lit$041847188$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Move tab to previous pane<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Hide comments<!--?lit$041847188$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Minimize comments<!--?lit$041847188$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Expand comments<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Code cell<!--?lit$041847188$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Text cell<!--?lit$041847188$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Section header cell<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Scratch code cell<!--?lit$041847188$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Code snippets<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Add a form field<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Run all<!--?lit$041847188$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Run before<!--?lit$041847188$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Run the focused cell<!--?lit$041847188$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Run selection<!--?lit$041847188$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Run cell and below<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Interrupt execution<!--?lit$041847188$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Restart session<!--?lit$041847188$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Restart session and run all<!--?lit$041847188$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Disconnect and delete runtime<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Change runtime type<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Manage sessions<!--?lit$041847188$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->View resources<!--?lit$041847188$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->View runtime logs<!--?lit$041847188$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Command palette<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2k" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Settings<!--?lit$041847188$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Keyboard shortcuts<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2n" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Diff notebooks<!--?lit$041847188$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$041847188$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$041847188$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Frequently asked questions<!--?lit$041847188$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->View release notes<!--?lit$041847188$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Search code snippets<!--?lit$041847188$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2t" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Report a bug<!--?lit$041847188$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Report Drive abuse<!--?lit$041847188$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->Send feedback<!--?lit$041847188$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$041847188$-->View terms of service<!--?lit$041847188$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$041847188$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$041847188$--><button id="button" class="button">
      <!--?lit$041847188$-->
      <span class="touch"></span>
      <!--?lit$041847188$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$041847188$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$041847188$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">YOUR_NGROK_AUTH_TOKEN</div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2864554004" name="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2864554004" src="./AttendanceSystem_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-vlcq4blugbnw" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./AttendanceSystem_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./AttendanceSystem_files/saved_resource.html"></iframe></div><iframe src="./AttendanceSystem_files/bscframe.html" style="display: none;"></iframe></body></html>