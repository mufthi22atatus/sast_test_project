/**
 * Trigger rules:
 *   - tg-js-prototype-pollution  (deep merge with user-controlled keys)
 * CWE-1321: Prototype Pollution
 */

// ── 🔴 Recursive merge without __proto__ check ────────────────────────────
function deepMerge(target, source) {
  for (const key in source) {
    // Missing: if (key === '__proto__' || key === 'constructor') continue;
    if (typeof source[key] === 'object' && source[key] !== null) {
      if (!target[key]) target[key] = {};
      deepMerge(target[key], source[key]);
    } else {
      target[key] = source[key]; // ❌ RULE HIT: tg-js-prototype-pollution
    }
  }
  return target;
}

// ── 🔴 Direct property assignment from user input ─────────────────────────
function setConfig(config, userInput) {
  for (const key of Object.keys(userInput)) {
    config[key] = userInput[key]; // ❌ RULE HIT: tg-js-prototype-pollution
  }
}

// ── Attack scenario ────────────────────────────────────────────────────────
// Attacker sends: { "__proto__": { "isAdmin": true } }
// After merge, ALL objects inherit isAdmin = true
const config = {};
const maliciousPayload = JSON.parse('{"__proto__": {"isAdmin": true}}');
deepMerge(config, maliciousPayload);

// Now any new object has isAdmin = true
const user = {};
console.log(user.isAdmin); // true — prototype polluted!

module.exports = { deepMerge, setConfig };
