"use strict";

document.addEventListener("DOMContentLoaded", async () => {
	const baseUrL = "http://localhost:8000";

	const response = await fetch(`${baseUrL}/shelters`);
	const shelters = await response.json();

	const contentElement = document.getElementById("shelters");
	for (let i in shelters) {
		const shelterElement = createShelterElement(shelters[i]);

		contentElement.appendChild(shelterElement);
	}
});

function createShelterElement(shelter) {
	const section = document.createElement("section");
	section.className = "card w-fit h-fit shadow-xl bg-zinc-900 py-4 px-6 m-5";
	section.innerHTML = `
		<h3 class="text-stone-300 font-bold text-xl">${shelter.name}</h3>
        <p class="text-sm">${shelter.address}</p>
        <div class="pt-3 flex flex-row h-full justify-around items-end">
          <div
            class="h-24 bg-zinc-800 rounded-2xl p-2 shadow-md w-28 m-2 flex flex-col items-center justify-between position-absolute hover:scale-105 transition-all">
            <p class="font-extrabold text-md">Dogs</p>
            <p class="mb-2 font-bold text-4xl">${shelter.animals.dogs}</p>
          </div>
          <div
            class="h-24 bg-zinc-800 rounded-2xl p-2 shadow-md w-28 m-2 flex flex-col items-center justify-between position-absolute hover:scale-105 transition-all">
            <p class="font-extrabold text-md">Cats</p>
            <p class="mb-2 font-bold text-4xl">${shelter.animals.cats}</p>
          </div>
        </div>`;

	return section;
}
