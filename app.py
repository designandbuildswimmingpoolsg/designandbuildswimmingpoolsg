import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Adding inline CSS for styling
st.markdown(
    """
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background-color: #cde2f7;
    }

    .landing-page {
        background-image: url('https://i.imgur.com/sBVacgd.png');
        background-repeat: no-repeat;
        background-position: center center;
        background-size: 300px;
        color: #fff;
        text-align: center;
        padding: 270px 0;
    }

    .landing-title {
        color: #007BFF;
    }

    .landing-text {
        color: #fff;
    }

    .page-link {
        text-decoration: none;
        color: #007BFF;
        cursor: pointer;
        margin-right: 20px;
        transition: color 0.3s ease-in-out;
    }

    .page-link:hover {
        color: #0056b3;
    }

    .column {
        float: left;
        width: 33.33%;
        padding: 5px;
    }

    /* Clearfix to prevent columns from wrapping */
    .row::after {
        content: "";
        clear: both;
        display: table;
    }
    <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11367889284">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-11367889284');
</script>
</style>
""",
    unsafe_allow_html=True,
)

def main():
    st.title("Build Your Dream Pool Now! ")
    st.header("Design & Build Swimming Pool Pte Ltd")
    pages = ["Home", "About Us", "Our Services", "Our Works", "Contact Us"]
    navigation = st.sidebar.radio("Navigation", pages)

    if navigation == "Home":
        st.markdown('<div class="landing-page">'
                    '</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="container">', unsafe_allow_html=True)

        if navigation == "About Us":
            st.markdown('<h2>About Us</h2>'
                        '<p>With 35 years of experience, we have been pioneers in the swimming pool industry, specializing in the design, construction, and maintenance of outdoor swimming pools and spas. Our commitment extends to both private and commercial clients, catering to their unique needs.</p>'
                        '<p>Recognizing the importance of environmental responsibility, we are dedicated to minimizing our impact by implementing energy-efficient control systems in all our pool installations. Our services encompass not only pool construction but also innovative design solutions, including features like moats and water features, setting us apart as industry leaders.</p>'
                        '<p>As experts in water treatment, we provide comprehensive swimming pool maintenance services, ensuring the longevity and performance of your pool.</p>', unsafe_allow_html=True)
            
        elif navigation == "Our Services":
            st.markdown('<h2>Our Services</h2>', unsafe_allow_html=True)
            st.markdown('<h3>Construction Specialist</h3>'
                        '<p>Construction Specialists have offered pool building services and maintenance since 1984, including for outdoor swimming pools and spas. We construct and provide servicing of swimming pools and spas for both private and commercial clients.</p>', unsafe_allow_html=True)
            st.markdown('<h3>Design & Construction</h3>'
                        '<p>At the forefront of technical developments, we offer bespoke swimming pool design and spa design services to meet the most challenging specifications and can include moats and water features.</p>', unsafe_allow_html=True)
            st.markdown('<h3>Maintenance & Water Treatment</h3>'
                        '<p>We are water treatment experts and provide a first-class swimming pool maintenance service, including one-off swimming pool cleaning as well as spa and hot tub maintenance.</p>', unsafe_allow_html=True)
            st.markdown('<ul>'
                '<li>Construction Progress</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/Onv4wU6.png" alt="Cons 1" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/1aOm9CT.png" alt="Cons 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/ok8vQwP.png" alt="Cons 3" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/pla0axK.png" alt="Cons 4" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/3RA5w5q.png" alt="Cons 5" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/XNQu3xS.png" alt="Cons 6" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/69ckAnx.png" alt="Cons 7" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/ncpS8rH.png" alt="Cons 8" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/o8X1Qp6.png" alt="Cons 9" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '</ul>', unsafe_allow_html=True)
        elif navigation == "Our Works":
            st.markdown('<h2>Explore our lineup of contemporary pool designs</h2>', unsafe_allow_html=True)
            st.markdown('<ul>'
                '<li>Small Residential Pool</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/Hy7EhtC.png" alt="Small Pool 1" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/Ia9Gzmp.jpg" alt="Small Pool 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/LDn4G03.jpg" alt="Small Pool 3" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/SDakhgd.jpg" alt="Small Pool 4" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/LxeEYxA.jpg" alt="Small Pool 5" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/8Zd70T4.png" alt="Small Pool 6" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/jJnzLM3.jpg" alt="Small Pool 13" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/7Ec493W.png" alt="Small Pool 14" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/dzCvD3M.jpg" alt="Small Pool 15" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<li>Large Residential Pool</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/sqmpQSq.png" alt="Large Pool 1" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/cy2xs7Y.jpg" alt="Large Pool 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/5GGcb0F.png" alt="Large Pool 3" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/IqStCBT.jpg" alt="Large Pool 4" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/ukkHbmw.jpg" alt="Large Pool 5" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/RPWrrk8.jpg" alt="Large Pool 6" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<li>Commercial Pool</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="" alt="" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/P9dwbZA.jpg" alt="Commercial Pool 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="" alt="" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '</li>'
                '<li>Fiber Glass Pool</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="" alt="" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/vIfoYMV.jpg" alt="Fiber Glass Pool 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="" alt="" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '</li>'
                '<li>Pool Slides</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/fQ6gVHZ.png" alt="Pool Slides 1" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/85oYUf6.png" alt="Pool Slides 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/V8JlPDI.png" alt="Pool Slides 3" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '</li>'
                '<li>Rockscape</li>'
                '<li>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/JLn2DMG.png" alt="Rockscape 1" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/8RjO0v4.png" alt="Rockscape 2" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/HMgmenb.png" alt="Rockscape 3" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '<div class="row">'
                '<div class="column">'
                '<img src="https://i.imgur.com/TKB3OAI.png" alt="Rockscape 4" style="max-width: 100%;">'
                '</div>'
                '<div class="column">'
                '<img src="https://i.imgur.com/tCuZFCI.png" alt="Rockscape 5" style="max-width: 100%;">'
                '</div>'
                '</div>'
                '</li>'
            '<li>Koi Pond</li>'
            '<li>'
            '<div class="row">'
            '<div class="column">'
            '<img src="" alt="" style="max-width: 100%;">'
            '</div>'
            '<div class="column">'
            '<img src="https://i.imgur.com/kbPwO3X.jpg" alt="Koi 2" style="max-width: 100%;">'
            '</div>'
            '<div class="column">'
            '<img src="" alt="" style="max-width: 100%;">'
            '</div>'
            '</div>'
            '</li>'
            '</ul>', unsafe_allow_html=True)
            st.markdown('<h4>Sample Projects Video</h4>', unsafe_allow_html=True)
                # Embed the YouTube video
            st.video('https://www.youtube.com/watch?v=VeFr89EG0MA')
                
        if navigation == "Contact Us":
            # Contact Form
            contact_form = """
            <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <select name="service" required>
                    <option value="" disabled selected>Select a service</option>
                    <option value="Pool Cleaning">Pool Cleaning</option>
                    <option value="Fiberglass Pool">Fiberglass Pool</option>
                    <option value="Exercise Pool">Exercise Pool</option>
                    <option value="Modular Pool">Modular Pool</option>
                    <option value="Swimming Pool Design">Swimming Pool Design</option>
                    <option value="Other/s (Please Specify)">Other/s (Please Specify)</option>
                </select>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            st.markdown(contact_form, unsafe_allow_html=True)

            # Add the address details and contact details
            st.markdown('<h2>Address</h2>'
                        '<p>Design & Build Swimming Pool Pte Ltd<br>'
                        'Address: 54 Lorong 28, Geylang, Singapore 398455<br>'
                        'Contact: +65.9455.6003 or +65.9166.6933​</p>', unsafe_allow_html=True)
        else:
            st.markdown('<h2>' + navigation + '</h2>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer" style="background-color: #333; color: #fff; padding: 10px; text-align: center;">'
                '<p>&copy; 2023 Design & Build Swimming Pool Pte Ltd</p>'
                '<p>Address: 54 Lorong 28, Geylang, Singapore 398455</p>'
                '<p>Contact: +65.9455.6003 or +65.9166.6933</p>'
                '</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
