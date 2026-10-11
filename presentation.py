from manim import *
from manim_slides import Slide


class CSIntro(Slide):
    def construct(self):
        # ---------------------------------------------------
        # SLIDE 1: IEEE CS Tanışma Toplantısı
        # ---------------------------------------------------

        # VISUALS: Create a cybernetic/engineering rotating tech ring
        ring1 = Circle(radius=1.5, color="#00629B", stroke_width=2)
        ring2 = DashedVMobject(
            Circle(radius=1.7, color="#FF9900", stroke_width=4), num_dashes=24
        )
        tech_rings = VGroup(ring1, ring2)

        # Attempt to load your actual CS logo (Make sure cs_logo.png is in this folder!)
        # If it's missing, it will fallback to stylized text so the code doesn't crash.
        try:
            logo = ImageMobject("assets/cs_logo.png").scale(0.9)
        except:  # noqa
            logo = Text("IEEE CS", font_size=48, weight=BOLD, color=WHITE)

        # Text Setup
        title = Text(
            "IEEE Computer Society", font_size=48, color="#00629B", weight=BOLD
        )
        subtitle = Text("Tanışma Toplantısı", font_size=36, color="#FF9900")
        title_group = (
            VGroup(title, subtitle).arrange(DOWN).next_to(tech_rings, DOWN, buff=0.5)
        )

        # ANIMATION SEQUENCE
        self.play(Create(tech_rings), run_time=1.5)
        self.play(FadeIn(logo))

        # Rotate the outer ring while writing the text to flex the animation engine
        self.play(Rotate(ring2, angle=PI / 2), Write(title_group), run_time=2)

        # BREAKPOINT 1
        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 2: Andrew Ng Quote
        # ---------------------------------------------------

        # Clean the screen smoothly
        self.play(FadeOut(logo), FadeOut(tech_rings), FadeOut(title_group))

        # Main Question
        q1 = Text(
            "AI Çağında Kodlama Öğrenmek Zorunda Mıyım?",
            font_size=36,
            color=WHITE,
            weight=BOLD,
        )
        self.play(Write(q1))

        # BREAKPOINT 2
        self.next_slide()

        # Shrink and push the question to the top of the screen
        self.play(q1.animate.scale(0.7).to_edge(UP))

        # The Quote
        ng_quote = Text(
            '"There will be no AI jobpocalypse.\n\n'
            "The story that AI will lead to massive unemployment is stoking\n"
            "unnecessary fear. AI — like any other technology — affects jobs,\n"
            "but telling overblown stories of large-scale unemployment is\n"
            'irresponsible and damaging. Let’s put a stop to it."',
            font_size=24,
            line_spacing=1.2,
            slant=ITALIC,
        )
        ng_author = Text(
            "— Andrew Ng, Founder of Google Brain",
            font_size=24,
            color="#FF9900",
            weight=BOLD,
        )

        # Group and align them cleanly to the right
        ng_group = VGroup(ng_quote, ng_author).arrange(
            DOWN, aligned_edge=RIGHT, buff=0.5
        )

        self.play(FadeIn(ng_quote, shift=UP))
        self.play(Write(ng_author))

        # BREAKPOINT 3
        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 3: Jensen Huang Quote
        # ---------------------------------------------------

        # Sweep the current slide completely off the screen to the left
        self.play(
            q1.animate.shift(LEFT * 15), ng_group.animate.shift(LEFT * 15), run_time=0.8
        )

        # Next Question flies in from the right
        q2 = Text(
            "Yapay Zeka İşimi Elimden Alacak Mı?",
            font_size=36,
            color=WHITE,
            weight=BOLD,
        )
        q2.shift(RIGHT * 15)

        self.play(q2.animate.move_to(ORIGIN), run_time=0.8)

        # BREAKPOINT 4
        self.next_slide()

        # Shrink and push to top
        self.play(q2.animate.scale(0.7).to_edge(UP))

        jensen_quote = Text(
            '"AI will not replace human jobs.\n'
            "It will replace parts of jobs.\n"
            'The people who win are the ones who learn to work with it."',
            font_size=28,
            line_spacing=1.2,
            slant=ITALIC,
        )

        # Nvidia Green for Jensen
        jensen_author = Text(
            "— Jensen Huang, CEO of Nvidia", font_size=24, color="#76B900", weight=BOLD
        )
        jensen_group = VGroup(jensen_quote, jensen_author).arrange(
            DOWN, aligned_edge=RIGHT, buff=0.5
        )

        self.play(FadeIn(jensen_quote, shift=UP))
        self.play(Write(jensen_author))

        # BREAKPOINT 5
        self.next_slide()

        # End presentation cleanly
        self.play(FadeOut(q2), FadeOut(jensen_group))

        # ---------------------------------------------------
        # SLIDE 4: The Pitch
        # ---------------------------------------------------

        # Visuals: Wrap the question in terminal-style HUD brackets
        left_bracket = Text("[", font_size=60, color="#FF9900")
        right_bracket = Text("]", font_size=60, color="#FF9900")
        q3 = Text(
            "Peki O Zaman Ne Yapmam Lazım?", font_size=40, color=WHITE, weight=BOLD
        )

        q3_group = VGroup(left_bracket, q3, right_bracket).arrange(RIGHT, buff=0.3)
        self.play(Write(q3_group))

        # BREAKPOINT 6
        self.next_slide()

        # Slide the question up, reveal the answer with a glowing tech box
        self.play(q3_group.animate.to_edge(UP))

        ans_box = RoundedRectangle(
            width=9, height=2, color="#00629B", fill_opacity=0.2, stroke_width=3
        )

        # Removed text_align and split into a
        # safely arranged VGroup for perfect centering
        ans_line1 = Text(
            "IEEE CS ile güvendesin!", font_size=36, color=WHITE, weight=BOLD
        )
        ans_line2 = Text("Hadi tanışalım!", font_size=36, color=WHITE, weight=BOLD)
        ans_text = VGroup(ans_line1, ans_line2).arrange(DOWN)

        ans_group = VGroup(ans_box, ans_text).move_to(ORIGIN)

        self.play(Create(ans_box), FadeIn(ans_text, shift=UP))

        # BREAKPOINT 7
        self.next_slide()

        # ---------------------------------------------------
        # UNIQUE TRANSITION: The Cyber Wipe
        # ---------------------------------------------------
        # A rapidly expanding ring that wipes the screen while the text collapses
        radar = Circle(radius=0.1, color="#FF9900", stroke_width=15)
        self.play(
            radar.animate.scale(150).set_opacity(0),
            q3_group.animate.scale(0),
            ans_group.animate.scale(0),
            run_time=0.7,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(q3_group, ans_group, radar)  # Clean memory

        # ---------------------------------------------------
        # SLIDE 5: Kim Bu Adamlar?
        # ---------------------------------------------------
        title_5 = Text(
            "Kim Bu Adamlar?", font_size=48, color="#FF9900", weight=BOLD
        ).to_edge(UP)
        self.play(Write(title_5))

        # Image Setup (Target positions centered side-by-side)
        target_ahmet = LEFT * 3.5 + UP * 0.5
        target_vp = RIGHT * 3.5 + UP * 0.5

        # Try to load real images.
        # If they aren't in the folder yet, generate placeholders.
        try:
            img_ahmet = ImageMobject("assets/ahmet.png").scale_to_fit_height(3.6)
        except:  # noqa
            img_ahmet = RoundedRectangle(
                width=3, height=4.5, color="#00629B", fill_opacity=0.2
            )
            img_ahmet.add(
                Text("Ahmet Tağluk\n(ahmet.png)", font_size=20, color=WHITE).move_to(
                    img_ahmet
                )
            )

        try:
            img_vp = ImageMobject("assets/arda.png").scale_to_fit_height(3.6)
        except:  # noqa
            img_vp = RoundedRectangle(
                width=3, height=4.5, color="#00629B", fill_opacity=0.2
            )
            img_vp.add(
                Text("Arda Yozgatlıgil\n(vp.png)", font_size=20, color=WHITE).move_to(
                    img_vp
                )
            )

        # Move them way off-screen to the right to prepare for the fly-in
        img_ahmet.move_to(RIGHT * 15 + UP * 0.5)
        img_vp.move_to(RIGHT * 15 + UP * 0.5)

        # THE ANIMATION: Fast in, overshoot, and snap back (ease_out_back)
        self.play(
            img_ahmet.animate.move_to(target_ahmet),
            img_vp.animate.move_to(target_vp),
            run_time=1.2,
            rate_func=rate_functions.ease_out_back,
        )

        # BREAKPOINT 8 (Wait for click before text cascade begins)
        self.next_slide()

        # The 6 Lines of Text
        left_texts = [
            "Başşşkan",
            "Ahmet Tağluk",
            "Way too OP",
            "Cooks Every Meal",
            "Top CENG Hater",
        ]

        right_texts = [
            "Başşkan Yardımcısı",
            "Arda Yozgatlıgil",
            "Way too Goated",
            "Serves Every Masterpiece",
            "Peak EEE Enjoyer",
        ]

        # Generate and align the text objects
        left_mobjects = VGroup(
            *[Text(t, font_size=22, color=WHITE) for t in left_texts]
        ).arrange(DOWN, buff=0.15)
        right_mobjects = VGroup(
            *[Text(t, font_size=22, color=WHITE) for t in right_texts]
        ).arrange(DOWN, buff=0.15)

        # Anchored to the physical image object's bottom edge,
        # not the center coordinate.
        left_mobjects.next_to(img_ahmet, DOWN, buff=0.5)
        right_mobjects.next_to(img_vp, DOWN, buff=0.5)

        # Color and bold the Titles and Names
        left_mobjects[0].set_color("#FF9900").set_weight(BOLD)
        left_mobjects[1].set_color("#00629B").set_weight(BOLD)
        right_mobjects[0].set_color("#FF9900").set_weight(BOLD)
        right_mobjects[1].set_color("#00629B").set_weight(BOLD)

        # The Cascade Loop: Animates both sides at the same time, row by row
        for i in range(5):
            self.play(
                FadeIn(left_mobjects[i], shift=UP * 0.2),
                FadeIn(right_mobjects[i], shift=UP * 0.2),
                run_time=0.4,
            )
            self.wait(0.1)

        # BREAKPOINT 9
        self.next_slide()

        # Clean up Slide 5
        self.play(
            FadeOut(title_5),
            FadeOut(img_ahmet),
            FadeOut(img_vp),
            FadeOut(left_mobjects),
            FadeOut(right_mobjects),
        )

        # ---------------------------------------------------
        # SLIDE 6: Ne Yaptık Bugüne Kadar?
        # ---------------------------------------------------

        # The Main Title
        title_6 = Text(
            "Ne Yaptık Bugüne Kadar?", font_size=48, color="#00629B", weight=BOLD
        ).to_edge(UP)
        self.play(Write(title_6))

        # --- 1. YAPAY ZEKA GÜNÜ ---
        try:
            img_yzg = ImageMobject("assets/yzg.png").scale_to_fit_height(4)
        except:  # noqa
            img_yzg = Rectangle(width=6, height=3.5, color="#FF9900", fill_opacity=0.2)
            img_yzg.add(
                Text("yzg.png\nPlaceholder", font_size=24, color=WHITE).move_to(img_yzg)
            )

        txt_yzg = Text("Yapay Zeka Günü", font_size=32, color=WHITE).next_to(
            img_yzg, DOWN
        )
        # FIXED: Using Group instead of VGroup for raster images
        grp_yzg = Group(img_yzg, txt_yzg).move_to(ORIGIN).shift(DOWN * 0.5)

        # Animation: Spiral in from nothing
        grp_yzg.scale(0.001)
        self.play(grp_yzg.animate.scale(1000).rotate(2 * PI), run_time=1)

        # BREAKPOINT 10
        self.next_slide()

        # --- 2. HACKMETU ---
        try:
            img_hack = ImageMobject("assets/hackmetu.png").scale_to_fit_height(4)
        except:  # noqa
            img_hack = Rectangle(width=6, height=3.5, color="#00629B", fill_opacity=0.2)
            img_hack.add(
                Text("hackmetu.png\nPlaceholder", font_size=24, color=WHITE).move_to(
                    img_hack
                )
            )

        txt_hack = Text("HackMETU", font_size=32, color=WHITE).next_to(img_hack, DOWN)
        grp_hack = Group(img_hack, txt_hack).move_to(ORIGIN).shift(DOWN * 0.5)

        # Animation: Sucked into a black hole, then explode outwards
        self.play(
            grp_yzg.animate.scale(0.001).rotate(-2 * PI),
            run_time=0.6,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(grp_yzg)  # Clean memory

        grp_hack.scale(0.001)
        self.play(
            grp_hack.animate.scale(1000),
            run_time=1.2,
            rate_func=rate_functions.ease_out_elastic,
        )

        # BREAKPOINT 11
        self.next_slide()

        # --- 3. TEA-TALKS ---
        try:
            img_tea1 = ImageMobject("assets/tea1.png").scale_to_fit_height(5)
        except:  # noqa
            img_tea1 = Rectangle(width=4, height=3.5, color="#FF9900", fill_opacity=0.2)
            img_tea1.add(Text("tea1.png", font_size=24, color=WHITE).move_to(img_tea1))

        try:
            img_tea2 = ImageMobject("assets/tea2.png").scale_to_fit_height(5)
        except:  # noqa
            img_tea2 = Rectangle(width=4, height=3.5, color="#00629B", fill_opacity=0.2)
            img_tea2.add(Text("tea2.png", font_size=24, color=WHITE).move_to(img_tea2))

        imgs_tea = Group(img_tea1, img_tea2).arrange(RIGHT, buff=1)
        txt_tea = Text("Tea-Talks", font_size=32, color=WHITE).next_to(imgs_tea, DOWN)
        grp_tea = Group(imgs_tea, txt_tea).move_to(ORIGIN).shift(DOWN * 0.5)

        # Animation: HackMETU falls off a cliff
        self.play(
            grp_hack.animate.shift(DOWN * 12).rotate(PI / 4),
            run_time=0.8,
            rate_func=rate_functions.ease_in_back,
        )
        self.remove(grp_hack)

        # Animation: Tea-Talks slam together from opposite sides
        target_tea1 = img_tea1.get_center()
        target_tea2 = img_tea2.get_center()

        img_tea1.move_to(LEFT * 12)
        img_tea2.move_to(RIGHT * 12)
        txt_tea.set_opacity(0)  # Hide text initially

        self.play(
            img_tea1.animate.move_to(target_tea1),
            img_tea2.animate.move_to(target_tea2),
            run_time=0.8,
            rate_func=rate_functions.ease_out_bounce,
        )
        self.play(txt_tea.animate.set_opacity(1), run_time=0.3)

        # BREAKPOINT 12
        self.next_slide()

        # --- 4. TEKNOFEST ---
        try:
            img_tekno = ImageMobject("assets/teknofest.png").scale_to_fit_height(5)
        except:  # noqa
            img_tekno = Rectangle(
                width=6, height=3.5, color="#00629B", fill_opacity=0.2
            )
            img_tekno.add(
                Text("teknofest.png\nPlaceholder", font_size=24, color=WHITE).move_to(
                    img_tekno
                )
            )

        txt_tekno = Text("TEKNOFEST Dereceleri", font_size=32, color=WHITE).next_to(
            img_tekno, DOWN
        )
        grp_tekno = Group(img_tekno, txt_tekno).move_to(ORIGIN).shift(DOWN * 0.5)

        # Animation: Tea-Talks swept away in a tornado
        self.play(
            grp_tea.animate.scale(0).rotate(3 * PI).shift(UP * 8),
            run_time=0.8,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(grp_tea)

        # Animation: Teknofest drops like an anvil
        target_tekno = grp_tekno.get_center()
        grp_tekno.shift(UP * 12)
        self.play(
            grp_tekno.animate.move_to(target_tekno),
            run_time=1.2,
            rate_func=rate_functions.ease_out_bounce,
        )

        # A little flex wiggle to emphasize the "Derece"
        self.play(Wiggle(grp_tekno), run_time=0.8)

        # BREAKPOINT 13
        self.next_slide()

        # Clean the screen for whatever comes next
        self.play(FadeOut(title_6), FadeOut(grp_tekno))

        # ---------------------------------------------------
        # SLIDE 7: Bu Sene Ne Yapacağız?
        # ---------------------------------------------------

        # 1. The Initial Title
        title_7 = Text(
            "Bu Sene Ne Yapacağız?", font_size=48, color="#00629B", weight=BOLD
        ).to_edge(UP)
        self.play(Write(title_7))

        # --- PART 1: Python & Workshops ---
        try:
            img_py = ImageMobject("assets/python_logo.png").scale_to_fit_height(2.5)
        except:  # noqa
            img_py = Rectangle(width=2.5, height=2.5, color="#FFD43B", fill_opacity=0.2)
            img_py.add(Text("python_logo.png", font_size=16).move_to(img_py))

        try:
            img_gh = ImageMobject("assets/github_logo.png").scale_to_fit_height(2.5)
        except:  # noqa
            img_gh = Rectangle(width=2.5, height=2.5, color=WHITE, fill_opacity=0.2)
            img_gh.add(Text("github_logo.png", font_size=16).move_to(img_gh))

        txt_py = Text("Python Eğitimleri", font_size=32, color=WHITE).next_to(
            img_py, DOWN
        )
        txt_gh = Text("Bombastik Workshoplar", font_size=32, color=WHITE).next_to(
            img_gh, DOWN
        )

        # Use Group instead of VGroup to safely handle the raster images
        grp_py = Group(img_py, txt_py).move_to(LEFT * 3.5)
        grp_gh = Group(img_gh, txt_gh).move_to(RIGHT * 3.5)

        # Move completely off-screen to prepare for the smash
        grp_py.shift(LEFT * 15)
        grp_gh.shift(RIGHT * 15)

        # The "Vine Boom" entry (Insanely fast and elastic snap into the center)
        self.play(
            grp_py.animate.move_to(LEFT * 3.5),
            grp_gh.animate.move_to(RIGHT * 3.5),
            run_time=0.7,
            rate_func=rate_functions.ease_out_elastic,
        )
        # Visual Impact effect (Flash and screen shake/wiggle)
        self.play(
            Flash(
                ORIGIN,
                line_length=3,
                num_lines=20,
                color="#FF9900",
                time_width=0.4,
                flash_radius=4,
            ),
            Wiggle(grp_py, run_time=0.4),
            Wiggle(grp_gh, run_time=0.4),
        )

        # BREAKPOINT 14
        self.next_slide()

        # Fly out rapidly to the corners
        self.play(
            grp_py.animate.shift(UP * 12).rotate(PI / 2),
            grp_gh.animate.shift(DOWN * 12).rotate(-PI / 2),
            run_time=0.6,
            rate_func=rate_functions.ease_in_back,
        )
        self.remove(grp_py, grp_gh)  # Clean memory

        # --- PART 2: The Teams Transformation ---
        title_teams = Text(
            "Takımlar, Takımlar ve Daha Çok Takımlar!",
            font_size=40,
            color="#FF9900",
            weight=BOLD,
        ).to_edge(UP)
        # Morph the old title into the new title seamlessly
        self.play(ReplacementTransform(title_7, title_teams))

        # --- TEAM 1: Open-Source (Text L, Image R) ---
        try:
            img_1 = ImageMobject("assets/linus.png").scale_to_fit_height(4)
        except:  # noqa
            img_1 = Rectangle(width=3, height=4, color="#00629B", fill_opacity=0.2)
            img_1.add(Text("linus.png", font_size=20).move_to(img_1))

        txt_1 = Text("Open-Source Ekibi", font_size=40, color=WHITE)
        grp_1 = (
            Group(txt_1, img_1).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Spiral in from a microdot
        grp_1.scale(0.001)
        self.play(
            grp_1.animate.scale(1000).rotate(4 * PI),
            run_time=0.8,
            rate_func=rate_functions.ease_out_back,
        )

        # BREAKPOINT 15
        self.next_slide()

        # Bombastic Exit: Sucked instantly into the left void
        self.play(
            grp_1.animate.shift(LEFT * 15).scale(0.001),
            run_time=0.5,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(grp_1)

        # --- TEAM 2: AI Ekibi (Image L, Text R) ---
        try:
            img_2 = ImageMobject("assets/jensen.png").scale_to_fit_height(4)
        except:  # noqa
            img_2 = Rectangle(width=3, height=4, color="#76B900", fill_opacity=0.2)
            img_2.add(Text("jensen.png", font_size=20).move_to(img_2))

        txt_2 = Text("Yapay Zeka Ekibi", font_size=40, color=WHITE)
        grp_2 = (
            Group(img_2, txt_2).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Bouncing drop from the ceiling
        grp_2.shift(UP * 12)
        self.play(
            grp_2.animate.move_to(DOWN * 0.5),
            run_time=0.8,
            rate_func=rate_functions.ease_out_bounce,
        )

        # BREAKPOINT 16
        self.next_slide()

        # Bombastic Exit: Spin away while shrinking
        self.play(
            grp_2.animate.scale(0.001).rotate(-2 * PI),
            run_time=0.5,
            rate_func=rate_functions.ease_in_back,
        )
        self.remove(grp_2)

        # --- TEAM 3: Oyun Geliştirme (Text L, Image R) ---
        try:
            img_3 = ImageMobject("assets/gamer.png").scale_to_fit_height(5)
        except:  # noqa
            img_3 = Rectangle(width=3, height=4, color="#E51400", fill_opacity=0.2)
            img_3.add(Text("gamer.png", font_size=20).move_to(img_3))

        txt_3 = Text("Oyun Geliştirme Ekibi", font_size=40, color=WHITE)
        grp_3 = (
            Group(txt_3, img_3).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Slam in from the right wall elastically
        grp_3.shift(RIGHT * 15)
        self.play(
            grp_3.animate.move_to(DOWN * 0.5),
            run_time=0.7,
            rate_func=rate_functions.ease_out_elastic,
        )

        # BREAKPOINT 17
        self.next_slide()

        # Bombastic Exit: Fall through the floor
        self.play(
            grp_3.animate.shift(DOWN * 12).rotate(-PI / 4),
            run_time=0.5,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(grp_3)

        # --- TEAM 4: Research Ekibi (Image L, Text R) ---
        try:
            img_4 = ImageMobject("assets/researcher.png").scale_to_fit_height(4)
        except:  # noqa
            img_4 = Rectangle(width=3, height=4, color="#68217A", fill_opacity=0.2)
            img_4.add(Text("researcher.png", font_size=20).move_to(img_4))

        txt_4 = Text("Research Ekibi", font_size=40, color=WHITE)
        grp_4 = (
            Group(img_4, txt_4).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Explode outwards from the center
        grp_4.scale(0.001)
        self.play(
            grp_4.animate.scale(1000),
            run_time=0.7,
            rate_func=rate_functions.ease_out_elastic,
        )

        # BREAKPOINT 18
        self.next_slide()

        # Bombastic Exit: Suck violently back into the center
        self.play(
            grp_4.animate.scale(0.001),
            run_time=0.4,
            rate_func=rate_functions.ease_in_expo,
        )
        self.remove(grp_4)

        # --- TEAM 5: Çip Tasarım Takımı (Text L, Image R) ---
        try:
            img_5 = ImageMobject("assets/captain.png").scale_to_fit_height(5)
        except:  # noqa
            img_5 = Rectangle(width=3, height=4, color="#A4C400", fill_opacity=0.2)
            img_5.add(Text("captain.png", font_size=20).move_to(img_5))

        txt_5 = Text("Çip Tasarım Takımı", font_size=40, color=WHITE)
        grp_5 = (
            Group(txt_5, img_5).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Slide in from the left wall, followed by a wiggle
        grp_5.shift(LEFT * 15)
        self.play(
            grp_5.animate.move_to(DOWN * 0.5),
            run_time=0.7,
            rate_func=rate_functions.ease_out_back,
        )
        self.play(Wiggle(grp_5, run_time=0.5))

        # BREAKPOINT 19
        self.next_slide()

        # Bombastic Exit: Shoot straight up through the ceiling
        self.play(
            grp_5.animate.shift(UP * 12).rotate(PI / 3),
            run_time=0.5,
            rate_func=rate_functions.ease_in_back,
        )
        self.remove(grp_5)

        # --- TEAM 6: TEKNOFEST Takımları (Image L, Text R) ---
        try:
            img_6 = ImageMobject("assets/me.png").scale_to_fit_height(5)
        except:  # noqa
            img_6 = Rectangle(width=3, height=4, color="#00629B", fill_opacity=0.2)
            img_6.add(Text("me.png", font_size=20).move_to(img_6))

        txt_6 = Text("TEKNOFEST Takımları", font_size=40, color=WHITE)
        grp_6 = (
            Group(img_6, txt_6).arrange(RIGHT, buff=1).move_to(ORIGIN).shift(DOWN * 0.5)
        )

        # Bombastic Entry: Mega Anvil Drop + Big Flash
        grp_6.shift(UP * 15)
        self.play(
            grp_6.animate.move_to(DOWN * 0.5),
            run_time=1.0,
            rate_func=rate_functions.ease_out_bounce,
        )
        self.play(
            Flash(grp_6, color="#00629B", line_length=3, num_lines=30), run_time=0.4
        )

        # BREAKPOINT 20
        self.next_slide()

        # Clean the screen for the next slide
        self.play(FadeOut(title_teams), FadeOut(grp_6))

        # ---------------------------------------------------
        # SLIDE 8: The Conclusion
        # ---------------------------------------------------

        # 1. The Main Text (Middle-Right)
        # Safely stacked using VGroup to avoid alignment errors
        txt_end1 = Text("Bugünlük Bu Kadar", font_size=44, color="#FF9900", weight=BOLD)
        txt_end2 = Text("Sunum Yeter", font_size=44, color="#00629B", weight=BOLD)
        txt_end = VGroup(txt_end1, txt_end2).arrange(DOWN).move_to(RIGHT * 3)

        # 2. The WhatsApp QR Code (Middle-Left)
        try:
            img_qr = ImageMobject("assets/whatsapp_qr.png").scale_to_fit_height(4.5)
        except:  # noqa
            img_qr = Rectangle(width=4.5, height=4.5, color="#00629B", fill_opacity=0.2)
            img_qr.add(
                Text("whatsapp_qr.png\nPlaceholder", font_size=20, color=WHITE).move_to(
                    img_qr
                )
            )

        # The Snowball Rolling Entrance Physics
        target_qr = LEFT * 3

        # Start tiny, off-screen left, and rotated backwards
        img_qr.move_to(LEFT * 12).scale(0.001).rotate(-4 * PI)

        self.play(Write(txt_end))

        # Roll it in!
        self.play(
            img_qr.animate.scale(1000).move_to(target_qr).rotate(4 * PI),
            run_time=1.5,
            rate_func=rate_functions.ease_out_bounce,
        )

        # BREAKPOINT 21
        self.next_slide()

        # 3. The Humorous Note (Bottom)
        txt_note = Text(
            "DİPNOT: Bu slayttaki görsellerde kimsenin rızası alınmamıştır.",
            font_size=24,
            color=GRAY,
            slant=ITALIC,
        )
        txt_note.to_edge(DOWN, buff=0.5)

        # Slide the joke up smoothly
        self.play(FadeIn(txt_note, shift=UP * 0.5))

        # BREAKPOINT 22
        self.next_slide()

        # 4. The Final CS Logo Pop
        # Clean the screen fast
        self.play(FadeOut(txt_end), FadeOut(img_qr), FadeOut(txt_note), run_time=0.4)

        # Attempt to load your real CS logo for the finale
        try:
            final_logo = ImageMobject("assets/cs_logo.png").scale_to_fit_height(4)
        except:  # noqa
            final_logo = Text("IEEE CS", font_size=72, weight=BOLD, color="#00629B")

        final_logo.scale(0.001)

        # Elastic snap into the center
        self.play(
            final_logo.animate.scale(1000),
            run_time=0.8,
            rate_func=rate_functions.ease_out_elastic,
        )

        # Final power wiggle
        self.play(Wiggle(final_logo, run_time=0.8))

        # BREAKPOINT 23 (The end of the presentation)
        self.next_slide()

        # Fade to black
        self.play(FadeOut(final_logo))
