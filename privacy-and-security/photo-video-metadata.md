# Photo and Video Metadata Removal

Purpose:      Detect hidden EXIF geolocation metrics and technical tracking tags embedded in media files, and strip them completely before publishing photos or videos online.
Requirements: Smartphone (iOS/Android), desktop operating system, or a local open-source file inspection utility.

---

## The Privacy Threat in Media Files

Whenever you capture a photo or shoot a video, your device silently stamps an underlying metadata profile right inside the file payload. For photos, this is stored as **EXIF (Exchangeable Image File Format)** data, while videos use structural container fields like **QuickTime User Data** or **RIFF Info Tags**. 

Without your knowledge, sharing a raw media file can expose:
*   **Exact Geolocation:** GPS latitude, longitude, and altitude tracking points that reveal where you live, work, or travel.
*   **Device Identity:** The specific smartphone or camera model, lens profile specifications, serial numbers, and internal software version.
*   **Timeline Metrics:** Precise calendar dates down to the exact second, along with local timezone offset configurations.

---

## How to Find Hidden Metadata Natively

You do not need programming knowledge to inspect these parameters. Standard operating system utilities can reveal this hidden tracking layer instantly.

### On Smartphones (iOS & Android)
1. Open your device's default gallery app (Photos or Google Photos).
2. Tap on any photo or video file.
3. Swipe up on the screen or tap the details button (represented by an "i" icon).
4. Scroll to view the technical hardware parameters and the interactive map location pin.

### On Desktop Systems (Windows & macOS)
*   **Windows:** Right-click the media file -> Select **Properties** -> Click the **Details** window tab to browse all structural descriptors.
*   **macOS:** Open the file in Preview or QuickTime player -> Press `Cmd + I` to open the Inspector panel -> Review the **Exif** or **Location** tab identifiers.

---

## Methods to Strip Metadata from Photos and Videos

Many communications apps (like Signal or WhatsApp) automatically compress and sanitize media files during transit. However, uploading assets directly to public cloud storage, open forums, community blogs, or Git repositories leaves the tracking footprint fully exposed.

### Method 1: Local Cross-Platform Software (Highly Secure)
To scrub your media assets in bulk on your own machine without routing personal data through third-party web servers:
*   **Desktop:** Use the open-source, industry-standard terminal engine **ExifTool** (supports hundreds of image and video file formats). Run this simple command to clear a file entirely:
    ```bash
    exiftool -all= video.mp4
    ```
*   **Mobile Apps:** Install data firewall utilities like **Scrambled EXIF** (Android) or **ViewExif** (iOS) to serve as a clean intermediary sharing layer.

### Method 2: Disabling Mobile Camera GPS Stamps Permanently
Prevent your mobile phone from capturing spatial location footprints inside your camera app entirely:
*   **iPhone:** Open System Settings -> Privacy & Security -> Location Services -> Camera -> Change authorization to **Never**.
*   **Android:** Open the native Camera application -> Access the Settings gear icon -> Toggle the **Save Location / Location Tags** setting to off.
