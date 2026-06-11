import { FacebookIcon, InstagramIcon, TwitterIcon, YoutubeIcon } from "lucide-react";

import Logo from "@/components/layout/logo";
import { Separator } from "@/components/ui/separator";

const Footer = () => {
  return (
    <footer>
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-3 px-4 py-4 max-md:flex-col sm:px-6 sm:py-6 md:gap-6 md:py-8">
        {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
        <a href="#">
          <div className="flex items-center gap-3">
            <Logo className="gap-3" />
          </div>
        </a>

        <div className="flex items-center gap-5 whitespace-nowrap">
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a className="opacity-80 transition-opacity duration-300 hover:opacity-100" href="#">
            About
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a className="opacity-80 transition-opacity duration-300 hover:opacity-100" href="#">
            Features
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a className="opacity-80 transition-opacity duration-300 hover:opacity-100" href="#">
            Works
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a className="opacity-80 transition-opacity duration-300 hover:opacity-100" href="#">
            Career
          </a>
        </div>

        <div className="flex items-center gap-4">
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a href="#">
            <FacebookIcon className="size-5" />
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a href="#">
            <InstagramIcon className="size-5" />
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a href="#">
            <TwitterIcon className="size-5" />
          </a>
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a href="#">
            <YoutubeIcon className="size-5" />
          </a>
        </div>
      </div>

      <Separator />

      <div className="mx-auto flex max-w-7xl justify-center px-4 py-8 sm:px-6">
        <p className="text-center font-medium text-balance">
          © 2026
          {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
          <a className="hover:underline" href="#">
            shadcn/studio
          </a>
          , Made with ❤️ for better web.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
