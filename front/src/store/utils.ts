export function slug(s: string): string {
  return s.toLowerCase().replace(/ /g, '-');
}

export default slug;
