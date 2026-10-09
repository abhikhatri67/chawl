(()=>{
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const hdr=$('header'),bar=$('#bar');
addEventListener('scroll',()=>{
  hdr.classList.toggle('s',scrollY>30);
  const h=document.documentElement;bar.style.width=(scrollY/(h.scrollHeight-innerHeight)*100)+'%';
},{passive:true});
$('#burger')?.addEventListener('click',()=>$('.links').classList.toggle('open'));
// reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
$$('.rv').forEach(el=>io.observe(el));
// counters
const co=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;co.unobserve(e.target);
  const t=+e.target.dataset.to,suf=e.target.dataset.suf||'',s=performance.now();
  (function f(n){const p=Math.min((n-s)/1600,1);e.target.textContent=Math.round(t*(1-Math.pow(1-p,4)))+suf;if(p<1)requestAnimationFrame(f)})(s);
}),{threshold:.5});
$$('[data-to]').forEach(el=>co.observe(el));
// cursor glow + card spotlight/tilt
const glow=$('#glow');
addEventListener('pointermove',e=>{if(glow){glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'}});
$$('.card').forEach(c=>{
  c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
    c.style.setProperty('--mx',x+'px');c.style.setProperty('--my',y+'px');
    c.style.transform=`perspective(900px) rotateX(${((y/r.height)-.5)*-6}deg) rotateY(${((x/r.width)-.5)*6}deg) translateY(-4px)`});
  c.addEventListener('pointerleave',()=>c.style.transform='');
});
// typed rotating word
const w=$('#word');if(w){const L=JSON.parse(w.dataset.words);let i=0;
  setInterval(()=>{w.style.opacity=0;setTimeout(()=>{i=(i+1)%L.length;w.textContent=L[i];w.style.opacity=1},300)},2600);w.style.transition='opacity .3s'}
// particle network
const cv=$('#net');
if(cv&&!matchMedia('(prefers-reduced-motion:reduce)').matches){
  const x=cv.getContext('2d');let W,H,P=[],m={x:-999,y:-999};
  const rs=()=>{W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight;
    P=Array.from({length:Math.min(110,W/13|0)},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5}))};
  rs();addEventListener('resize',rs);
  cv.parentElement.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();m.x=e.clientX-r.left;m.y=e.clientY-r.top});
  (function draw(){x.clearRect(0,0,W,H);
    P.forEach((p,i)=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;
      const dm=Math.hypot(p.x-m.x,p.y-m.y);if(dm<160){p.x+=(p.x-m.x)/dm*1.5;p.y+=(p.y-m.y)/dm*1.5}
      x.fillStyle='rgba(0,229,195,.8)';x.beginPath();x.arc(p.x,p.y,1.8,0,7);x.fill();
      for(let j=i+1;j<P.length;j++){const d=Math.hypot(p.x-P[j].x,p.y-P[j].y);
        if(d<130){x.strokeStyle=`rgba(124,92,255,${.45*(1-d/130)})`;x.beginPath();x.moveTo(p.x,p.y);x.lineTo(P[j].x,P[j].y);x.stroke()}}});
    requestAnimationFrame(draw)})();
}
// contact form -> opens mail client (no backend needed); swap for Formspree/your API later
const f=$('#cform');
if(f)f.addEventListener('submit',e=>{e.preventDefault();
  if(f.website.value)return;
  const d=new FormData(f),body=`Name: ${d.get('name')}\nCompany: ${d.get('company')}\nEmail: ${d.get('email')}\nInterest: ${d.get('topic')}\n\n${d.get('message')}`;
  location.href=`mailto:hello@chawl.in?subject=${encodeURIComponent('Project enquiry: '+d.get('topic'))}&body=${encodeURIComponent(body)}`;
  $('#fmsg').textContent='Opening your email app… you can also write to hello@chawl.in directly.';
});
})();
