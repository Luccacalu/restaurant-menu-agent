import streamlit as st
from core.vectorstore import get_chroma_collection
from services.query_execution_service import execute_query_plan
from uuid import uuid4
from services.ingest_service import ingest_menu_item
from services.query_planner import build_query_plan

def get_all_menu_items(niche="restaurant"):
    collection = get_chroma_collection(niche)
    data = collection.get()

    items = []

    for id_, doc, meta in zip(
        data["ids"],
        data["documents"],
        data["metadatas"]
    ):
        items.append({
            "id": id_,
            "document": doc,
            "metadata": meta
        })

    return items

st.set_page_config(
    page_title="Restaurant Menu RAG",
    layout="wide"
)

st.title("🍽️ Restaurant Menu RAG")

mode = st.sidebar.radio(
    "Mode",
    ["User", "Admin"]
)

if mode == "User":
    st.subheader("🍽️ Ask about the menu")

    question = st.text_input(
        "Your question",
        placeholder="Do you have vegan dishes under $20?"
    )

    if question:
        with st.spinner("Thinking..."):

            plan = build_query_plan(question)

            answer = execute_query_plan(
                question=question,
                niche="restaurant",
                plan=plan,
            )

        st.markdown("### Answer")
        st.write(answer)

if mode == "Admin":
    data = get_all_menu_items()

    if not data:
        st.info("No menu items yet.")
    else:
        for item in data:
            meta = item["metadata"]
            id_ = item["id"]
            st.markdown(f"""
            **{meta.get('name', 'Unnamed')}**
            - ID: `{id_}`
            - Category: {meta.get('category')}
            - Description: {item['document']}
            - Diet: {meta.get('diet')}
            - Ingredients: {meta.get('ingredients')}
            - Price: ${meta.get('price')}
            """)

    st.divider()
    st.subheader("➕ Add new menu item")

    with st.form("add_menu_item"):
        name = st.text_input("Name")
        description = st.text_area("Description")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            category = st.selectbox(
                "Category",
                ["main_course", "appetizer", "dessert"]
            )

        with col2:
            diet = st.selectbox(
                "Diet",
                ["omnivore", "vegetarian", "vegan"]
            )

        with col3:
            price = st.number_input(
                "Price",
                min_value=0.0,
                step=1.0
            )

        with col4:
            ingredients_text = st.text_area(
                "Ingredients (one per line or comma-separated)",
                help="Example: rice, lemon zest, olive oil"
            )

        submitted = st.form_submit_button("Add item")

        if submitted:
            if not name or not description:
                st.error("Name and description are required.")
            else:

                ingredients = [
                    i.strip()
                    for i in ingredients_text.replace("\n", ",").split(",")
                    if i.strip()
                ]

                item_id = str(uuid4())

                ingest_menu_item(
                    id=item_id,
                    name=name,
                    description=description,
                    category=category,
                    diet=diet,
                    price=price,
                    ingredients=ingredients
                )

                st.success(f"Item '{name}' added successfully!")
                st.rerun()

    st.subheader("📋 Edit current menu items")

    items = get_all_menu_items()

    if not items:
        st.info("No menu items yet.")

    for item in items:
        meta = item["metadata"]
        item_id = item["id"]

        with st.expander(meta.get("name", "Unnamed"), expanded=False):

            name = st.text_input(
                "Name",
                value=meta.get("name", "Unnamed"),
                key=f"name_{item_id}"
            )

            description = st.text_area(
                "Description",
                value=item["document"],
                key=f"desc_{item_id}"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                category = st.selectbox(
                    "Category",
                    ["main_course", "appetizer", "dessert"],
                    index=["main_course", "appetizer", "dessert"].index(meta["category"]),
                    key=f"cat_{item_id}"
                )

            with col2:
                diet = st.selectbox(
                    "Diet",
                    ["omnivore", "vegetarian", "vegan"],
                    index=["omnivore", "vegetarian", "vegan"].index(meta["diet"]),
                    key=f"diet_{item_id}"
                )

            with col3:
                price = st.number_input(
                    "Price",
                    value=float(meta["price"]),
                    step=1.0,
                    key=f"price_{item_id}"
                )
            
            with col4:
                ingredients_text = st.text_area(
                    "Ingredients",
                    value=meta.get("ingredients", ""),
                    key=f"ing_{item_id}",
                    help="Comma-separated or one per line"
                )

            col_update, col_delete = st.columns(2)

            with col_update:
                if st.button("💾 Save changes", key=f"save_{item_id}"):
                    ingredients = [
                        i.strip()
                        for i in ingredients_text.replace("\n", ",").split(",")
                        if i.strip()
                    ]

                    ingest_menu_item(
                        id=item_id,
                        name=name,
                        description=description,
                        category=category,
                        diet=diet,
                        price=price,
                        ingredients=ingredients
                    )
                    st.success("Updated successfully")
                    st.rerun()

            with col_delete:
                if st.button("🗑️ Delete item", key=f"del_{item_id}"):
                    collection = get_chroma_collection("restaurant")
                    collection.delete(ids=[item_id])
                    st.warning("Item deleted")
                    st.rerun()

