import asyncio
import edge_tts

async def generate_long_speech(text: str, voice: str, output_path: str):
    """Generates long-form speech using Microsoft Edge's advanced AI voices."""
    print(f"🤖 Initializing male voice [{voice}] for long audio generation...")
    
    # Configure the TTS engine
    communicate = edge_tts.Communicate(text, voice)
    
    print("⏳ Processing and saving your audio file (this may take a minute for long text)...")
    # Save the file directly to the cloud container
    await communicate.save(output_path)
    
    print(f"✨ Success! Audio file saved to: {output_path}")

if __name__ == "__main__":
    # --- CONFIGURATION ZONE ---
    
    # 1. SELECT YOUR MALE VOICE HERE:
    # For English (US Male), use: "en-US-BrianNeural" or "en-US-ChristopherNeural"
    # For Hindi (India Male), use: "hi-IN-MadhurNeural" 
    SELECTED_VOICE = "en-US-BrianNeural" 
    
    # 2. PASTE YOUR LONG TEXT HERE (Can be 6 to 10 minutes long):
    SAMPLE_TEXT = """
**BHAGAVAD GITA – CHAPTER 1, VERSE 4**
**Extended Cinematic Narration (English Version – Approximately 5 Minutes)**

**Narrator (deep, resonant voice):**

"Kurukshetra...

The Field of Dharma.

For generations, this sacred land had witnessed the rise and fall of kings, the performance of ancient sacrifices, and the footsteps of sages seeking truth. Yet on this day, it would bear witness to something far greater—the greatest war ever fought in the memory of mankind.

The first light of dawn spreads slowly across the horizon. Dust hangs in the cool morning air. Thousands upon thousands of warriors stand assembled beneath fluttering banners. Horses stamp the earth impatiently. Elephants, clad in armor, await the command to advance. Chariots line the vast battlefield like waves upon an endless sea.

Two mighty armies face one another.

Brothers against brothers.

Teachers against students.

Friends against friends.

Bound by blood... divided by destiny.

Among the Kaurava ranks stands Duryodhana, heir to the throne of Hastinapura. Proud, intelligent, and ambitious, he surveys the opposing army with a calculating gaze. He knows the stakes of this war. He understands that victory will not come easily.

Before him stands the formidable host of the Pandavas.

And within that host are warriors whose very names command respect.

As his eyes scan the battlefield, Duryodhana speaks.

'Here stand heroes... mighty bowmen... equal in battle to Bhima and Arjuna.'

These are not ordinary men.

These are Maharathas—great chariot warriors capable of confronting thousands of opponents at once.

The first among them is Yuyudhana.

Known throughout Aryavarta as Satyaki.

A warrior of the Vrishni clan.

A devoted disciple of Arjuna.

Loyalty defines his character. Courage shapes his actions. In him burns an unshakable commitment to righteousness.

He stands upon his chariot, bow in hand, his gaze fixed steadily upon the enemy before him.

His armor gleams beneath the rising sun.

Every arrow in his quiver has been placed with meticulous care.

Every movement reflects years of discipline and training.

He does not fight for glory.

He does not seek personal gain.

He fights because he believes that justice must prevail.

Beside him stand the warriors of Matsya.

At their head is King Virata.

The noble ruler who once opened the doors of his kingdom to the exiled Pandavas.

When fate compelled the sons of Pandu to conceal their identities during the final year of exile, it was Virata who unknowingly sheltered them.

Now the time for concealment has passed.

The time for courage has arrived.

Virata ascends his royal chariot.

The white horses before him rear against the morning sky.

His banner dances in the wind.

Though age has touched his face, it has not diminished the strength within his heart.

He understands the price of this conflict.

He knows that war spares no family and honors no crown.

Yet he has chosen his path.

He stands for gratitude.

He stands for loyalty.

He stands for Dharma.

And then there is Drupada.

The mighty king of Panchala.

A ruler whose life has been shaped by friendship, betrayal, and the relentless currents of destiny.

Once, he and Drona shared the bond of companionship.

But time transformed friendship into enmity.

Humiliation gave birth to vengeance.

And vengeance altered the course of countless lives.

Yet Drupada is more than the sum of old grievances.

He is a seasoned warrior.

A father.

A king.

A Maharatha whose reputation has spread across the kingdoms of Bharatavarsha.

His beard bears the marks of age.

His eyes reveal the wisdom earned through suffering.

He knows that every decision carries consequences.

Even so, he stands ready.

Ready to defend those he believes to be rightful heirs.

Ready to fulfill the duties imposed upon him by honor and circumstance.

Duryodhana sees them all.

Satyaki.

Virata.

Drupada.

Names spoken with admiration by allies and caution by foes.

These men possess strength equal to Bhima, whose mace can shatter armies.

They possess skill comparable to Arjuna, whose mastery of archery is unmatched.

They are heroes.

Mighty bowmen.

Great chariot warriors.

And they stand united beneath the banner of the Pandavas.

The realization settles heavily upon Duryodhana's mind.

This war will not be won through numbers alone.

For courage cannot be counted.

Conviction cannot be measured.

And righteousness cannot be subdued by force alone.

Across the battlefield, thousands await the inevitable.

Some fight for duty.

Some for loyalty.

Some for ambition.

Some for revenge.

Each heart carries its own burden.

Each soul wrestles with its own questions.

What is justice?

What is honor?

What is the cost of righteousness?

What sacrifices must one make in the pursuit of duty?

Soon, the conches will sound.

Soon, arrows will darken the sky.

Soon, the earth of Kurukshetra will drink the blood of kings and commoners alike.

Yet before the first weapon is raised...

Before the first charge begins...

There exists this moment.

A moment of stillness.

A moment of recognition.

A moment in which one prince acknowledges the greatness of those who oppose him.

And above the chaos yet to unfold stands a truth far greater than victory or defeat.

For the battlefield of Kurukshetra is not merely a place upon the earth.

It is a reflection of the human condition itself.

Within every heart exists a struggle between fear and courage...

between selfish desire and selfless duty...

between confusion and wisdom.

The warriors assembled here represent more than armies.

They represent choices.

Values.

Principles.

And the eternal quest to understand what it truly means to live according to Dharma.

As the sun rises higher above the sacred plain, destiny moves steadily forward.

The heroes take their positions.

The chariot wheels stand ready.

The conches await their call.

And humanity stands upon the threshold of one of its greatest spiritual revelations.

For from this battlefield...

from the uncertainty of conflict...

from the questions that arise within the heart of a warrior...

will emerge a timeless message.

A dialogue that will transcend generations.

A teaching that will illuminate the path of seekers for ages to come.

But before those sacred words are spoken...

before the song of the Divine is heard...

the world pauses to behold these heroes.

The mighty bowmen.

The steadfast kings.

The great chariot warriors.

Yuyudhana.

Virata.

Drupada.

Their names echo across the field of Kurukshetra.

Their choices shape the course of history.

And their presence reminds us that true greatness lies not merely in strength of arms...

but in the courage to stand for what one believes to be right.

'Here stand heroic warriors, mighty bowmen equal to Bhima and Arjuna in battle—Yuyudhana, Virata, and Drupada, the great chariot warrior.'

Thus begins the journey.

Thus begins the Bhagavad Gita.

And the greatest battle...

has only just begun."

    """
    
    # 3. NAME YOUR OUTPUT FILE:
    OUTPUT_FILE = "long_english_male.mp3"
    
    # Run the async system required by edge-tts
    asyncio.run(generate_long_speech(SAMPLE_TEXT, SELECTED_VOICE, OUTPUT_FILE))

