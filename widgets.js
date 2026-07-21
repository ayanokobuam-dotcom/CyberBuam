/* widgets.js — reusable interactive lesson widgets for cyberbuam
   Each render function takes (container, data) and mounts itself. */
(function(global){
  "use strict";

  function el(tag, cls, html){
    var e = document.createElement(tag);
    if(cls) e.className = cls;
    if(html !== undefined) e.innerHTML = html;
    return e;
  }

  function click(node, fn){ node.addEventListener("click", fn); }

  /* ---------------- hotspot-diagram ---------------- */
  function renderHotspot(container, data){
    var wrap = el("div", "wd-hotspot wd-layout-" + (data.layout || "scatter"));
    var grid = el("div", "wd-hotspot-grid");
    var detail = el("div", "wd-hotspot-detail");
    detail.innerHTML = '<p class="wd-hint">Tap a piece to learn what it does.</p>';

    data.items.forEach(function(item, i){
      var chip = el("button", "wd-chip");
      chip.type = "button";
      chip.innerHTML =
        '<span class="wd-chip-icon">' + item.icon + '</span>' +
        '<span class="wd-chip-label">' + item.label + '</span>' +
        '<span class="wd-chip-short">' + item.short + '</span>';
      if(data.layout === "stack") chip.style.setProperty("--depth", i);
      click(chip, function(){
        Array.prototype.forEach.call(grid.children, function(c){ c.classList.remove("active"); });
        chip.classList.add("active");
        detail.innerHTML =
          '<div class="wd-detail-title">' + item.icon + ' ' + item.label + '</div>' +
          '<div class="wd-detail-body">' + item.detail + '</div>';
      });
      grid.appendChild(chip);
    });

    wrap.appendChild(grid);
    wrap.appendChild(detail);
    container.appendChild(wrap);
  }

  /* ---------------- step-flow ---------------- */
  function renderStepFlow(container, data){
    var wrap = el("div", "wd-stepflow");
    var stage = el("div", "wd-stepflow-stage");
    var rail = el("div", "wd-stepflow-rail");
    var controls = el("div", "wd-stepflow-controls");
    var idx = 0;
    var playing = false;
    var timer = null;

    var dots = data.steps.map(function(_, i){
      var d = el("span", "wd-rail-dot" + (i === 0 ? " active" : ""));
      rail.appendChild(d);
      return d;
    });

    var linkflow = data.mode === "linkflow";
    var stageBody;
    if(linkflow){
      stageBody = el("div", "wd-linkflow");
      var a = el("div", "wd-actor wd-actor-a", '<span>' + (data.actors && data.actors[0] || "Client") + '</span>');
      var b = el("div", "wd-actor wd-actor-b", '<span>' + (data.actors && data.actors[1] || "Server") + '</span>');
      var track = el("div", "wd-linkflow-track");
      var packet = el("div", "wd-packet", "📨");
      track.appendChild(packet);
      stageBody.appendChild(a);
      stageBody.appendChild(track);
      stageBody.appendChild(b);
    }

    var textBox = el("div", "wd-step-text");

    function renderStep(){
      var step = data.steps[idx];
      dots.forEach(function(d, i){ d.classList.toggle("active", i === idx); d.classList.toggle("done", i < idx); });
      textBox.innerHTML =
        '<div class="wd-step-title">' + (step.icon || "") + ' ' + step.title + '</div>' +
        '<div class="wd-step-detail">' + step.detail + '</div>';
      if(linkflow){
        var goingRight = step.from === "client";
        packet.textContent = step.icon || "📨";
        packet.classList.remove("wd-packet-fwd", "wd-packet-back");
        void packet.offsetWidth; // restart animation
        packet.classList.add(goingRight ? "wd-packet-fwd" : "wd-packet-back");
      }
      prevBtn.disabled = idx === 0;
      nextBtn.textContent = idx === data.steps.length - 1 ? "Restart" : "Next →";
    }

    var prevBtn = el("button", "wd-btn wd-btn-ghost", "← Prev");
    prevBtn.type = "button";
    var nextBtn = el("button", "wd-btn", "Next →");
    nextBtn.type = "button";
    var playBtn = el("button", "wd-btn wd-btn-ghost", "▶ Play");
    playBtn.type = "button";

    click(prevBtn, function(){ if(idx > 0){ idx--; renderStep(); } });
    click(nextBtn, function(){
      idx = (idx + 1) % data.steps.length;
      renderStep();
    });
    click(playBtn, function(){
      playing = !playing;
      playBtn.textContent = playing ? "⏸ Pause" : "▶ Play";
      if(playing){
        timer = setInterval(function(){
          idx = (idx + 1) % data.steps.length;
          renderStep();
        }, 2600);
      } else {
        clearInterval(timer);
      }
    });

    controls.appendChild(prevBtn);
    controls.appendChild(playBtn);
    controls.appendChild(nextBtn);

    stage.appendChild(rail);
    if(linkflow) stage.appendChild(stageBody);
    stage.appendChild(textBox);
    stage.appendChild(controls);
    wrap.appendChild(stage);
    container.appendChild(wrap);
    renderStep();
  }

  /* ---------------- flip-cards ---------------- */
  function renderFlipCards(container, data){
    var wrap = el("div", "wd-flipcards");
    data.cards.forEach(function(c){
      var card = el("div", "wd-flipcard");
      var inner = el("div", "wd-flipcard-inner");
      var front = el("div", "wd-flipcard-face wd-flipcard-front", c.front);
      var back = el("div", "wd-flipcard-face wd-flipcard-back", c.back);
      inner.appendChild(front);
      inner.appendChild(back);
      card.appendChild(inner);
      click(card, function(){ card.classList.toggle("flipped"); });
      wrap.appendChild(card);
    });
    container.appendChild(wrap);
  }

  /* ---------------- matching ---------------- */
  function shuffle(arr){
    var a = arr.slice();
    for(var i = a.length - 1; i > 0; i--){
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function renderMatching(container, data){
    var wrap = el("div", "wd-matching");
    var status = el("div", "wd-matching-status", "Match every pair — 0 / " + data.pairs.length);
    var cols = el("div", "wd-matching-cols");
    var leftCol = el("div", "wd-matching-col");
    var rightCol = el("div", "wd-matching-col");

    var leftItems = shuffle(data.pairs.map(function(p, i){ return {text: p.left, i: i}; }));
    var rightItems = shuffle(data.pairs.map(function(p, i){ return {text: p.right, i: i}; }));

    var selectedLeft = null, selectedRight = null, matched = 0;

    function makeBtn(item, side){
      var btn = el("button", "wd-match-btn", item.text);
      btn.type = "button";
      click(btn, function(){
        if(btn.classList.contains("matched")) return;
        if(side === "left"){
          if(selectedLeft) selectedLeft.el.classList.remove("selected");
          selectedLeft = {el: btn, i: item.i};
          btn.classList.add("selected");
        } else {
          if(selectedRight) selectedRight.el.classList.remove("selected");
          selectedRight = {el: btn, i: item.i};
          btn.classList.add("selected");
        }
        if(selectedLeft && selectedRight){
          if(selectedLeft.i === selectedRight.i){
            selectedLeft.el.classList.add("matched");
            selectedRight.el.classList.add("matched");
            selectedLeft.el.classList.remove("selected");
            selectedRight.el.classList.remove("selected");
            matched++;
            status.textContent = matched === data.pairs.length
              ? "🎉 All matched!"
              : "Match every pair — " + matched + " / " + data.pairs.length;
            selectedLeft = null; selectedRight = null;
          } else {
            var l = selectedLeft.el, r = selectedRight.el;
            l.classList.add("wrong"); r.classList.add("wrong");
            setTimeout(function(){
              l.classList.remove("wrong", "selected");
              r.classList.remove("wrong", "selected");
            }, 420);
            selectedLeft = null; selectedRight = null;
          }
        }
      });
      return btn;
    }

    leftItems.forEach(function(item){ leftCol.appendChild(makeBtn(item, "left")); });
    rightItems.forEach(function(item){ rightCol.appendChild(makeBtn(item, "right")); });

    cols.appendChild(leftCol);
    cols.appendChild(rightCol);
    wrap.appendChild(status);
    wrap.appendChild(cols);
    container.appendChild(wrap);
  }

  var renderers = {
    "hotspot-diagram": renderHotspot,
    "step-flow": renderStepFlow,
    "flip-cards": renderFlipCards,
    "matching": renderMatching,
  };

  function renderInteractive(container, block){
    var section = el("section", "wd-block");
    section.appendChild(el("h4", "wd-block-title", block.title || ""));
    var body = el("div", "wd-block-body");
    section.appendChild(body);
    var fn = renderers[block.type];
    if(fn) fn(body, block);
    container.appendChild(section);
  }

  global.cyberWidgets = { renderInteractive: renderInteractive };
})(window);
