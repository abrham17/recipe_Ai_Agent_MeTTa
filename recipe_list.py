from hyperon import MeTTa, E, S

metta = MeTTa()

# Recipe 1: Injera
recipe_one = E(
    S("Injera"),
    E(
        S("Ingrients"),
        S("0.48 kg teff flour"),
        S("0.72 l water"),
        S("0.002 kg salt (added after fermentation)")
    ),
    E(
        S("process"),
        S("1. In a large bowl, whisk together teff flour and water until smooth. Cover and let sit at room temperature (or in a warm area) for 2–3 days until batter becomes slightly bubbly and sour-smelling."),
        S("2. Stir in salt just before cooking."),
        S("3. Preheat a nonstick griddle or skillet over medium heat. When hot, pour a ladleful (about 80 ml) of batter in a circular motion to form a thin, crepe-like circle."),
        S("4. Cover the skillet with a lid and cook for 2–3 minutes, until holes form on the surface and edges lift slightly. Do not flip."),
        S("5. Gently remove injera with a spatula and set aside. Repeat until all batter is used.")
    ),
    E(S("Injera"), S("time"), S("180"))
)
metta.space().add_atom(recipe_one)

# Recipe 2: Doro Wat
recipe_two = E(
    S("Doro Wat"),
    E(
        S("Ingrients"),
        S("1.50 kg whole chicken (cut into pieces)"),
        S("0.80 kg onions (finely chopped)"),
        S("0.042 kg niter kibbeh (Ethiopian spiced butter)"),
        S("0.024 kg berbere spice mix"),
        S("0.030 kg tomato paste"),
        S("0.020 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("0.24 l chicken broth or water"),
        S("Salt, to taste"),
        S("6–8 eggs, hard-boiled (optional)")
    ),
    E(
        S("process"),
        S("1. In a heavy pot, sauté chopped onions (no oil) over medium-low heat, stirring constantly, until they release moisture and begin to turn golden brown—about 15–20 minutes."),
        S("2. Add niter kibbeh and continue to sauté for another 5 minutes."),
        S("3. Stir in minced garlic and ginger; cook 2 minutes more."),
        S("4. Add berbere spice and tomato paste. Cook, stirring, for 3–4 minutes until fragrant."),
        S("5. Add chicken pieces and mix well to coat with the onion–spice base. Season with salt."),
        S("6. Pour in chicken broth (or water) and bring to a gentle simmer. Cover and cook for 40–50 minutes, stirring occasionally."),
        S("7. If using, add hard-boiled eggs in the last 10 minutes to heat through."),
        S("8. Adjust seasoning and serve hot atop injera.")
    ),
    E(S("time"), S("120"))
)
metta.space().add_atom(recipe_two)

# Recipe 3: Misir Wat
recipe_three = E(
    S("Misir Wat"),
    E(
        S("Ingrients"),
        S("0.30 kg red lentils (rinsed)"),
        S("0.30 kg onions (finely chopped)"),
        S("0.028 kg niter kibbeh"),
        S("0.016 kg berbere spice mix"),
        S("0.015 kg tomato paste"),
        S("0.015 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("0.72 l water or vegetable broth"),
        S("Salt, to taste")
    ),
    E(
        S("process"),
        S("1. In a pot, sauté chopped onions (no oil) over medium heat until soft and translucent, about 8–10 minutes."),
        S("2. Add niter kibbeh and continue to sauté onions for another 3–4 minutes."),
        S("3. Stir in minced garlic and ginger; cook for 2 minutes."),
        S("4. Add berbere and tomato paste; cook, stirring, for 2–3 minutes until fragrant."),
        S("5. Add rinsed lentils and pour in water or broth. Bring to a boil, then reduce heat to low."),
        S("6. Simmer, uncovered, stirring occasionally, until lentils are tender and the stew is thick—about 25–30 minutes."),
        S("7. Season with salt, adjust consistency by adding a splash of water if too thick, and serve over injera.")
    ),
    E(S("time"), S("60"))
)
metta.space().add_atom(recipe_three)

# Recipe 4: Shiro Wat
recipe_four = E(
    S("Shiro Wat"),
    E(
        S("Ingrients"),
        S("0.32 kg shiro powder (ground chickpeas or broad beans)"),
        S("0.30 kg onions (finely chopped)"),
        S("0.042 kg niter kibbeh"),
        S("0.016 kg berbere spice mix"),
        S("0.015 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("0.96 l water or broth"),
        S("Salt, to taste")
    ),
    E(
        S("process"),
        S("1. In a saucepan, sauté chopped onions (no oil) over medium heat until soft, about 8 minutes."),
        S("2. Add niter kibbeh and continue cooking onions for 3–4 minutes."),
        S("3. Stir in minced garlic and ginger; cook for another 2 minutes."),
        S("4. Add berbere spice; stir and cook for 2–3 minutes until it becomes very fragrant."),
        S("5. Slowly sprinkle shiro powder into the pot while whisking to avoid lumps."),
        S("6. Pour in water or broth gradually, stirring constantly until it forms a smooth mixture."),
        S("7. Bring to a gentle simmer and cook 10–12 minutes, stirring frequently so it doesn’t stick. The stew should thicken to a pudding-like consistency."),
        S("8. Season with salt, adjust thickness with a little more water if needed, and serve steaming hot on injera.")
    ),
    E(S("time"), S("45"))
)
metta.space().add_atom(recipe_four)

# Recipe 5: Tibs
recipe_five = E(
    S("Tibs"),
    E(
        S("Ingrients"),
        S("0.45 kg beef or lamb (cubed)"),
        S("0.028 kg niter kibbeh"),
        S("0.20 kg onion (sliced)"),
        S("0.20 kg tomatoes (chopped)"),
        S("0.010 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("2 green chilies, sliced (optional)"),
        S("0.002 kg paprika (or mild chili powder)"),
        S("Salt and pepper, to taste"),
        S("0.004 kg fresh rosemary or basil (chopped, optional)")
    ),
    E(
        S("process"),
        S("1. In a large skillet or cast-iron pan, heat niter kibbeh over medium-high heat until melted."),
        S("2. Add cubed meat and sear, stirring occasionally, until browned on all sides—about 5–7 minutes."),
        S("3. Add sliced onions and cook until translucent, about 5 minutes."),
        S("4. Stir in minced garlic, ginger, and paprika; cook 2 minutes until fragrant."),
        S("5. Mix in chopped tomatoes and green chilies; cook until tomatoes soften, about 4–5 minutes."),
        S("6. Season with salt, pepper, and fresh herbs (if using). Continue to sauté for another 2–3 minutes."),
        S("7. Taste and adjust seasoning. Serve hot on injera or with rice.")
    ),
    E(S("time"), S("35"))
)
metta.space().add_atom(recipe_five)

# Recipe 6: Kitfo
recipe_six = E(
    S("Kitfo"),
    E(
        S("Ingrients"),
        S("0.45 kg lean beef (finely minced or ground)"),
        S("0.042 kg niter kibbeh"),
        S("0.008–0.016 kg mitmita (Ethiopian chili powder) or to taste"),
        S("0.015 kg awaze (berbere paste with honey and water)"),
        S("Salt, to taste"),
        S("Optional: ayib (Ethiopian cheese) and gomen (greens) on the side")
    ),
    E(
        S("process"),
        S("1. In a mixing bowl, combine minced beef with mitmita, awaze, and a pinch of salt."),
        S("2. In a small saucepan, warm niter kibbeh over low heat until melted (do not let it brown)."),
        S("3. Pour warm niter kibbeh over the spiced meat mixture and gently fold to combine. Do not cook beyond very lightly warming the meat—kitfo is traditionally served very rare or ‘mild’ (lightly sautéed)."),
        S("4. Serve immediately on injera with a side of ayib and gomen if desired.")
    ),
    E(S("time"), S("15"))
)
metta.space().add_atom(recipe_six)

# Recipe 7: Atakilt Wat
recipe_seven = E(
    S("Atakilt Wat"),
    E(
        S("Ingrients"),
        S("0.14 kg cabbage (chopped)"),
        S("0.10 kg carrot (sliced)"),
        S("0.30 kg potatoes (peeled and cubed)"),
        S("0.028 kg niter kibbeh"),
        S("0.20 kg onion (chopped)"),
        S("0.010 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("0.003 kg turmeric powder"),
        S("0.24 l water or vegetable broth"),
        S("Salt and pepper, to taste")
    ),
    E(
        S("process"),
        S("1. In a pot, heat niter kibbeh over medium heat. Add chopped onions and sauté until translucent, about 5–7 minutes."),
        S("2. Stir in minced garlic and ginger; cook 2 minutes until fragrant."),
        S("3. Add turmeric powder and stir to coat onions, cooking another minute."),
        S("4. Add potatoes and carrots; cook, stirring, for 3–4 minutes."),
        S("5. Pour in water or broth, bring to a simmer, then cover and cook for 10 minutes."),
        S("6. Add chopped cabbage, stir, cover again, and cook for 10–12 minutes until vegetables are tender but not mushy."),
        S("7. Season with salt and pepper. Serve warm on injera.")
    ),
    E(S("time"), S("50"))
)
metta.space().add_atom(recipe_seven)

# Recipe 8: Gomen (already provided, included for completeness)
recipe_eight = E(
    S("Gomen"),
    E(
        S("Ingrients"),
        S("0.45 kg collard greens or kale (stems removed and leaves chopped)"),
        S("0.028 kg niter kibbeh"),
        S("0.20 kg onions (chopped)"),
        S("0.010 kg garlic (minced)"),
        S("0.015 kg ginger (minced)"),
        S("0.24 l water or vegetable broth"),
        S("Salt and pepper, to taste")
    ),
    E(
        S("process"),
        S("1. In a large pot, heat niter kibbeh over medium heat. Add chopped onions and cook until soft and translucent, about 5 minutes."),
        S("2. Add minced garlic and ginger; stir and cook for 2 minutes."),
        S("3. Add chopped collard greens (or kale) and stir to coat with spiced butter."),
        S("4. Pour in water or broth, cover, and reduce heat to low. Cook, stirring occasionally, for 15–20 minutes until greens are tender."),
        S("5. Season with salt and pepper, taste and adjust. Serve hot on injera or alongside tibs.")
    ),
    E(S("time"), S("30"))
)
metta.space().add_atom(recipe_eight)