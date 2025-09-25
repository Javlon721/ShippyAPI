

const BASE_URL = "http://localhost:8000";

function get_modifiers_by(type) {
  return [...document.querySelectorAll(`[data-modifier='${type}'] .case-card input`)]
    .reduce((acc, item) => {
      if (item.checked) {
        acc.push(item.value);
      }
      return acc;
    }, []);
}


function getModifierNode(data) {
  return `
        <label class="case-card">
          <input
            type="checkbox"
            name="cases"
            value='${data.name}'
          />
          <div class="case-info">
            <strong>${data.name}</strong>
            <small>
              ${data.desc}
            </small>
          </div>
    </label>
  `;
}

async function fetchAvailableModifiers() {
  try {
    const resp = await fetch(BASE_URL + "/modifier");

    if (!resp.ok) {
      console.log('Modifiers didnt fetched');
    }

    const modifiers = await resp.json();

    const attackParent = document.querySelector("[data-modifier='attack']");
    const defenceParent = document.querySelector("[data-modifier='defence']");

    for (const i in modifiers) {
      const modifier = modifiers[i];
      switch (modifier.type) {
        case "attack":
          attackParent.innerHTML += getModifierNode(modifier);
          break;
        case "defence":
          defenceParent.innerHTML += getModifierNode(modifier);
          break;
        default:
          console.log("there is no", modifier.name);
      }


    }

  } catch (error) {
    console.log(error);
  }
}


async function main() {
  await fetchAvailableModifiers();
  await form_logic();
}


async function form_logic() {
  document
    .getElementById('shipForm')
    .addEventListener('submit', async (e) => {
      e.preventDefault();
      const form = e.target;


      // Разбиваем и берем только name
      const attack_modifiers = get_modifiers_by("attack");
      const defence_modifiers = get_modifiers_by("defence");


      const data = {
        ship_id: form.ship_id.value,
        ship_name: form.ship_name.value || null,
        hp: parseInt(form.hp.value),
        damage: parseInt(form.damage.value),
        velocity: parseFloat(form.velocity.value),
        ship_type: form.ship_type.value || null,
        nation: form.nation.value || null,
        attack_range: parseFloat(form.attack_range.value),
        modifiers: {
          attack_modifiers,
          defence_modifiers,
        },
      };

      try {
        const res = await fetch(BASE_URL + '/ship', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });
        const result = await res.json();
        document.getElementById('response').textContent = JSON.stringify(
          result,
          null,
          2
        );
        form.reset();
      } catch (err) {
        document.getElementById('response').textContent =
          'Ошибка: ' + err.message;
      }
    });
}

document.addEventListener("DOMContentLoaded", main);