import flet as ft

def main(page: ft.Page):
    page.title = "Navy Fuel Calculator Pro"
    page.background_image_src = "https://images.unsplash.com/photo-1544945582-108713023f73?q=80&w=2071&auto=format&fit=crop"
    page.background_image_fit = "cover"
    
    # Page alignment အတွက် ပုံစံအသစ်
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    distance = ft.TextField(label="အကွာအဝေး (မိုင်)", width=280, bgcolor="white")
    speed_per_hour = ft.TextField(label="တစ်နာရီမိုင်နှုန်း", width=280, bgcolor="white")
    engine_consumption = ft.TextField(label="အင်ဂျင် တစ်နာရီဆီစားနှုန်း", width=280, bgcolor="white")
    engine_count = ft.TextField(label="အင်ဂျင် အရေအတွက်", width=280, bgcolor="white")
    gen_consumption = ft.TextField(label="မီးစက် တစ်နာရီဆီစားနှုန်း", width=280, bgcolor="white")
    blower_consumption = ft.TextField(label="လေသွင်းစက် တစ်နာရီဆီစားနှုန်း", width=280, bgcolor="white")
    
    result_text = ft.Text(value="စုစုပေါင်း လိုအပ်မည့်ဆီ -", size=20, weight="bold", color="yellow")

    def calculate(e):
        try:
            d = float(distance.value)
            s = float(speed_per_hour.value)
            e_c = float(engine_consumption.value)
            e_n = float(engine_count.value)
            g_c = float(gen_consumption.value)
            b_c = float(blower_consumption.value)
            
            total_hours = d / s
            total_fuel = (total_hours * e_c * e_n) + (total_hours * g_c) + (4 * b_c)
            
            result_text.value = f"စုစုပေါင်း လိုအပ်မည့်ဆီ: {round(total_fuel, 2)} ဂါလန်"
        except:
            result_text.value = "အချက်အလက်များ မှန်ကန်စွာ ထည့်သွင်းပါ!"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Navy Fuel Calculator", size=28, weight="bold", color="white"),
                distance, speed_per_hour, engine_consumption, engine_count, gen_consumption, blower_consumption,
                # ElevatedButton အစား Button ကို သုံးလိုက်ပါပြီ
                ft.ElevatedButton("တွက်ချက်မည်", on_click=calculate),
                result_text
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
            bgcolor=ft.Colors.with_opacity(0.6, "black"),
            padding=20, 
            border_radius=20,
            # alignment ပြဿနာကိုဖြေရှင်းရန် ဒီနေရာကို ဖယ်လိုက်ပါတယ်
        )
    )

# Version အသစ်အတွက် run() ကို သုံးလိုက်ပါပြီ
ft.app(target=main, port=8000, view=ft.AppView.FLET_APP_WEB)
